#!/usr/bin/env python3
"""
Extract a compact, pair-safe DetectRL-X ternary dataset.

Example:
  python extract_ternary_subset.py trinary_general_256_open.json \
      --lang english --domains academic,wiki \
      --train-per-domain 1000 --test-per-domain 250 \
      --out ternary_academic_wiki_256.csv

The requested cap is per domain and per supplied split, NOT per model.
Within each domain/split, records are selected round-robin across models
(after reservoir sampling within each model cell) to reduce model imbalance.

Each source observation produces up to three rows:
  human, ai_generated, ai_refined

All rows from one source observation share pair_id and retain the source split.
"""
import argparse
import csv
import random
import sys
from collections import Counter, defaultdict

import ijson


def records(path):
    """Stream records from a top-level JSON array."""
    with open(path, "rb") as f:
        for i, item in enumerate(ijson.items(f, "item", use_float=True)):
            yield i, item


def canonical_domain(value):
    """Normalize common spelling variants for filtering only."""
    value = str(value or "").strip().lower()
    if value in {"wiki", "wikipedia"}:
        return "wiki"
    if value in {"academic", "academia"}:
        return "academic"
    return value


def scan(path):
    counts = Counter()
    for i, rec in records(path):
        key = (
            str(rec.get("lang", "")).lower(),
            canonical_domain(rec.get("domain")),
            str(rec.get("model", "unknown")),
            str(rec.get("split", "")).lower(),
        )
        counts[key] += 1
        if (i + 1) % 20000 == 0:
            print(f"Scanned {i + 1:,} source observations...", file=sys.stderr)

    print(f"Total source observations: {sum(counts.values()):,}")
    for lang in sorted({k[0] for k in counts}):
        print(f"\n[{lang}]")
        for domain in sorted({k[1] for k in counts if k[0] == lang}):
            print(f"  domain={domain!r}")
            for split in sorted({k[3] for k in counts if k[0] == lang and k[1] == domain}):
                cells = [(k[2], n) for k, n in counts.items()
                         if k[0] == lang and k[1] == domain and k[3] == split]
                print(f"    split={split}: " +
                      ", ".join(f"{model}={n}" for model, n in sorted(cells)))


def unpack(rec, pair_id):
    common = {
        "pair_id": pair_id,
        "lang": rec.get("lang"),
        "model": rec.get("model"),
        "domain": rec.get("domain"),
        "split": rec.get("split"),
    }
    fields = [
        ("human", "human_written_text"),
        ("ai_generated", "llm_generated_text"),
        ("ai_refined", "llm_refined_text"),
    ]
    for label, field in fields:
        text = rec.get(field)
        if isinstance(text, str) and text.strip():
            yield {**common, "label": label, "text": text.strip()}


def reservoir_add(bucket, item, seen, cap, rng):
    """Reservoir sampling into one (split, domain, model) bucket."""
    seen += 1
    if len(bucket) < cap:
        bucket.append(item)
    else:
        j = rng.randrange(seen)
        if j < cap:
            bucket[j] = item
    return seen


def balanced_select(cell_items, target, rng):
    """
    Select up to target records round-robin across model cells.
    Randomize within each cell so selection is not tied to source ordering.
    """
    keys = sorted(cell_items, key=str)
    pools = {}
    for key in keys:
        pool = list(cell_items[key])
        rng.shuffle(pool)
        pools[key] = pool

    selected = []
    while len(selected) < target:
        progressed = False
        for key in keys:
            if pools[key] and len(selected) < target:
                selected.append(pools[key].pop())
                progressed = True
        if not progressed:
            break
    return selected


def extract(args):
    rng = random.Random(args.seed)
    wanted_domains = {canonical_domain(d) for d in args.domains.split(",") if d.strip()}
    targets = {"train": args.train_per_domain, "test": args.test_per_domain}

    # (split, canonical_domain, model) -> reservoir of source records
    reservoirs = defaultdict(list)
    seen = Counter()

    for i, rec in records(args.path):
        if str(rec.get("lang", "")).strip().lower() != args.lang.lower():
            continue
        domain = canonical_domain(rec.get("domain"))
        if domain not in wanted_domains:
            continue
        split = str(rec.get("split", "")).strip().lower()
        if split not in targets:
            continue
        target = targets[split]
        if target <= 0:
            continue

        model = str(rec.get("model") or "unknown")
        cell = (split, domain, model)
        seen[cell] = reservoir_add(
            reservoirs[cell], (i, rec), seen[cell], target, rng
        )

    chosen = []
    summary = {}
    for split in ("train", "test"):
        for domain in sorted(wanted_domains):
            cells = {
                (s, d, m): items
                for (s, d, m), items in reservoirs.items()
                if s == split and d == domain
            }
            # Remove split/domain from keys for balanced_select; model is the key.
            by_model = {key[2]: items for key, items in cells.items()}
            selected = balanced_select(by_model, targets[split], rng)
            chosen.extend(selected)
            summary[(split, domain)] = len(selected)

    output_fields = ["text", "label", "pair_id", "lang", "model", "domain", "split"]
    label_counts, split_counts, domain_counts = Counter(), Counter(), Counter()
    source_pairs = 0
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=output_fields)
        writer.writeheader()
        for pair_id, rec in sorted(chosen, key=lambda x: x[0]):
            source_pairs += 1
            for row in unpack(rec, pair_id):
                writer.writerow({k: row.get(k) for k in output_fields})
                label_counts[row["label"]] += 1
                split_counts[row["split"]] += 1
                domain_counts[canonical_domain(row["domain"])] += 1

    print(f"\nWrote {sum(label_counts.values()):,} text rows from {source_pairs:,} source pairs to {args.out}")
    print("Selected source pairs by split/domain:")
    for key, count in sorted(summary.items()):
        print(f"  {key[0]}/{key[1]}: {count:,}")
    print("Text rows by label:", dict(label_counts))
    print("Text rows by split:", dict(split_counts))
    print("Text rows by domain:", dict(domain_counts))
    if not source_pairs:
        print("No records matched. Run --scan and check exact language/domain/split values.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Path to the ternary JSON array")
    parser.add_argument("--scan", action="store_true", help="Print available language/domain/model/split counts")
    parser.add_argument("--lang", default="english")
    parser.add_argument("--domains", default="academic,wiki")
    parser.add_argument("--train-per-domain", type=int, default=1000,
                        help="Maximum source observations per domain in supplied train split")
    parser.add_argument("--test-per-domain", type=int, default=250,
                        help="Maximum source observations per domain in supplied test split")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out", default="ternary_academic_wiki_256.csv")
    args = parser.parse_args()

    if args.train_per_domain < 0 or args.test_per_domain < 0:
        parser.error("sample caps must be non-negative")
    if args.scan:
        scan(args.path)
    else:
        extract(args)


if __name__ == "__main__":
    main()

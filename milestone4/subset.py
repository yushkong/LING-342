#!/usr/bin/env python3
"""Stream one DetectRL-X JSON file and keep only the slice you need.

The files are ~1-1.4 GB JSON arrays, so this never loads the whole file:
it streams records with ijson and keeps only the ones that match.

Install:   pip install ijson huggingface_hub

1) Download ONE file (about 1.26 GB), not the whole 33 GB repo:
   python -c "from huggingface_hub import hf_hub_download as d; \
print(d('WUJUNCHAO/DetectRL-X', 'Ternary/trinary_general_open.json', repo_type='dataset'))"

2) See what is inside (languages / domains / models / splits):
   python sample_detectrl_x.py PATH_TO_JSON --scan

3) Extract a slice as one labelled row per text:
   python sample_detectrl_x.py PATH_TO_JSON --lang english \
       --domains "News,SomeOtherDomain" --out english_slice.csv

Output columns: text, label, pair_id, lang, model, domain, split
  label    = human | ai_generated | ai_refined (ai_refined only in Ternary files)
  pair_id  = row index in the source file. The human / generated / refined
             texts of one record share a pair_id, so never split rows of the
             same pair_id across train and test. Use the provided `split`
             column as-is.
"""
import argparse
import csv
import random
import sys
from collections import Counter, defaultdict

import ijson


def records(path):
    """Yield records one at a time from a top-level JSON array."""
    with open(path, "rb") as f:
        for i, item in enumerate(ijson.items(f, "item", use_float=True)):
            yield i, item


def scan(path):
    counts = Counter()
    for i, rec in records(path):
        counts[(rec.get("lang"), rec.get("domain"), rec.get("model"), rec.get("split"))] += 1
        if (i + 1) % 20000 == 0:
            print(f"  scanned {i + 1:,} records...", file=sys.stderr)
    langs = sorted({k[0] for k in counts})
    print(f"\nTotal records: {sum(counts.values()):,}")
    for lang in langs:
        print(f"\n[{lang}]")
        by_domain = defaultdict(Counter)
        for (l, dom, model, split), n in counts.items():
            if l == lang:
                by_domain[dom][(model, split)] += n
        for dom in sorted(by_domain, key=str):
            total = sum(by_domain[dom].values())
            models = sorted({m for m, _ in by_domain[dom]}, key=str)
            print(f"  domain={dom!r}: {total:,} records; models={models}")


def unpack(rec, pair_id):
    base = {k: rec.get(k) for k in ("lang", "model", "domain", "split")}
    base["pair_id"] = pair_id
    yield {**base, "label": "human", "text": rec.get("human_written_text", "")}
    yield {**base, "label": "ai_generated", "text": rec.get("llm_generated_text", "")}
    if rec.get("llm_refined_text"):
        yield {**base, "label": "ai_refined", "text": rec["llm_refined_text"]}


def extract(path, lang, domains, models, max_per_cell, seed, out):
    rng = random.Random(seed)
    lang = lang.lower()
    domains = {d.strip().lower() for d in domains} if domains else None
    models = {m.strip().lower() for m in models} if models else None

    kept = defaultdict(list)   # (split, model, domain) -> [(pair_id, rec)]
    seen = Counter()
    for i, rec in records(path):
        if str(rec.get("lang", "")).lower() != lang:
            continue
        if domains and str(rec.get("domain", "")).lower() not in domains:
            continue
        if models and str(rec.get("model", "")).lower() not in models:
            continue
        cell = (rec.get("split"), rec.get("model"), rec.get("domain"))
        seen[cell] += 1
        if max_per_cell is None or len(kept[cell]) < max_per_cell:
            kept[cell].append((i, rec))
        else:  # reservoir sampling keeps a uniform random subset per cell
            j = rng.randrange(seen[cell])
            if j < max_per_cell:
                kept[cell][j] = (i, rec)

    fields = ["text", "label", "pair_id", "lang", "model", "domain", "split"]
    n_rows, label_counts, split_counts, words = 0, Counter(), Counter(), 0
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for cell in sorted(kept, key=str):
            for pair_id, rec in kept[cell]:
                for row in unpack(rec, pair_id):
                    w.writerow({k: row[k] for k in fields})
                    n_rows += 1
                    label_counts[row["label"]] += 1
                    split_counts[row["split"]] += 1
                    words += len(str(row["text"]).split())
    print(f"Wrote {n_rows:,} rows to {out}")
    print("  by label:", dict(label_counts))
    print("  by split:", dict(split_counts))
    if n_rows:
        print(f"  mean words per text: {words / n_rows:.1f}")
    if not n_rows:
        print("No rows matched. Run with --scan to check the exact lang/domain strings.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help="local path to a DetectRL-X *_open.json file")
    ap.add_argument("--scan", action="store_true", help="list languages/domains/models and exit")
    ap.add_argument("--lang", default="english")
    ap.add_argument("--domains", default="", help="comma-separated domain names (empty = all)")
    ap.add_argument("--models", default="", help="comma-separated model names (empty = all four)")
    ap.add_argument("--max-per-cell", type=int, default=None,
                    help="optional cap of records per (split, model, domain)")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="slice.csv")
    a = ap.parse_args()
 
    if a.scan:
        scan(a.path)
    else:
        extract(
            a.path, a.lang,
            [d for d in a.domains.split(",") if d],
            [m for m in a.models.split(",") if m],
            a.max_per_cell, a.seed, a.out,
        )
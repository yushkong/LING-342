This repository provides Milestones 4, 5, and 6 for **Team Awesome (Emily Chen 52998994, Yushan Jiang 37847761)**.

In `\milestone4`, please find three baseline models based on pre-existing models for discriminiating human-written vs. AI-generated vs. AI-refined texts. 

The `.md` files `Quantitative-Analysis_baseline.md` and `Qualitative-Analysis_baseline.md` contain reports for quantitative and qualitative analysis of our baseline models, respectively.

# Baseline Models

For our baselines we used 2 approaches: Lexical and Contextual. The descriptions of the baselines we used is as follows:

* **TF-IDF baseline**: converts text into TF-IDF-weighted lexical features, followed by Logistic Regression. This does not have a token limit. For ease of comparison, since our second approach does require truncation, we included a truncated and non-truncated version of this model.
* **Frozen RoBERTa**: extracts contextual representations from a pretrained RoBERTa model without updating its parameters, followed by a trained classifier. BERT has a 512-token limit, so the input to RoBERTa needs to be truncated. As a result, we include two RoBERTa baseline models with different truncation limits: 256 and 512. 

## DataSet
The datasets for baseline experiment can either be downloaded from [Google Drive](https://drive.google.com/drive/folders/1K_8WyErnWsxsAE9Qa9P-HCkbdql8KrCX?usp=sharing), or streamed from [HuggingFace](https://huggingface.co/datasets/WUJUNCHAO/DetectRL-X/tree/main/Ternary) (See the Python script in `milestone4/` to generate a subset of obeservations with equally distributed domain weights).
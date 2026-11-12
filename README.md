This repository provides Milestones 4, 5, and 6 for **Team Awesome (Emily Chen 52998994, Yushan Jiang 37847761)**.

In `\milestone4`, please find three baseline models based on pre-existing models for discriminiating human-written vs. AI-generated vs. AI-refined texts. 

The `.md` files `milestone5.md` and `milestone6.md` contain reports for quantitative and qualitative analysis of our baseline models, respectively.

# Baseline Models

For our baselines we used 2 approaches: Lexical and Contextual. The descriptions of the baselines we used is as follows:

* TF-IDF baseline: converts text into TF-IDF-weighted lexical features, followed by Logistic Regression. This does not have a token limit.
* Frozen RoBERTa: extracts contextual representations from a pretrained RoBERTa model without updating its parameters, followed by a trained classifier. BERT has a 512-token limit, so the input to RoBERTa needs to be truncated. As a result, we include two RoBERTa baseline models with different truncation limits: 256 and 512. 

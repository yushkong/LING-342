# Quantitative Analysis

For each model, we looked at accuracy, precision, recall, and Macro-F1.
* Justify why these metrics were chosen

For the non-truncated TF-IDF Logistic Regression model, we found:

accuracy | macro-F1
---
0.8657 | 0.8637

| precision | recall | F1-score
---
human | 0.8263 | 0.8965 | 0.8600
ai_generated | 0.9144 | 0.9555 | 0.9345
ai_refined | 0.8563 | 0.7450 | 0.7968 
weighted avg | 0.8656 | 0.8657 | 0.8637

![Confuction Matrix](images\confmatrix_tf-idfbaseline.png)

* Brief escription:

For the truncated TF-IDF Logistic Regression model, we found:
* Table:
* Confusion matrix:
* Brief escription:

For Frozen RoBERTa with a truncation limit of 256, we found:
* Table:
* Confusion matrix:
* Brief escription:

For Frozen RoBERTa with a truncation limit of 512, we found:
* Table:
* Confusion matrix:
* Brief escription:

Comparison between 3 models, describe strengths and weaknesses of each. Explain possible reasons.

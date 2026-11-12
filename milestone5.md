# Quantitative Analysis

For each model, we looked at accuracy, precision, recall, and Macro-F1. For each class, we looked at precision, recall, and F1 as well.    

* **Accuracy** was selected as a big-picture measure of performance.
* **Macro-F1** was selected as an overview of per-class F1 scores for a balanced look at how the models perform in terms of precision and recall. **F1** was also calculated for each class for a more individual look at what classes the models perform better at.
* **Precision and recall** were selected to get a better idea of what types of error each model tends to produce. These were looked at both on average and for individual classes for a closer look.


### For the non-truncated TF-IDF Logistic Regression model:

#### On Average:

| accuracy | macro-F1 | precision | recall |
| --- | --- | --- | --- |
| 0.8657 | 0.8637 | 0.8656 | 0.8657 |

#### Per-Class:

| | precision | recall | F1-score |
| --- | --- | --- | --- |
| human | 0.8263 | 0.8965 | 0.8600 |
| ai_generated | 0.9144 | 0.9555 | 0.9345 |
| ai_refined | 0.8563 | 0.7450 | 0.7968  |



![Confusion Matrix](/images/confmatrix_tf-idfbaseline.png)

* Brief 

### For the truncated TF-IDF Logistic Regression model:

#### On Average:

| accuracy | macro-F1 | precision | recall |
| --- | --- | --- | --- |
| 0.7947 | 0.7961 | 0.8072 | 0.7947 |

#### Per-Class:

| | precision | recall | F1-score |
| --- | --- | --- | --- |
| human | 0.8110 | 0.8580 | 0.8338 |
| ai_generated | 0.9148 | 0.7300 | 0.8120 |
| ai_refined | 0.6958 | 0.7960 | 0.7425 |

![Confusion Matrix](/images/confmatrix_tf-idftruncated.png)

* Brief escription:

### For Frozen RoBERTa with a truncation limit of 256:

#### On Average:

| accuracy | macro-F1 | precision | recall |
| --- | --- | --- | --- |
| 0.8820 | 0.8837 | 0.8937 | 0.8820 |

#### Per-Class:

| | precision | recall | F1-score |
| --- | --- | --- | --- |
| human | 0.9135 | 0.9080 | 0.9107 |
| ai_generated | 0.9880 | 0.8260 | 0.8998 |
| ai_refined | 0.7795 | 0.9120 | 0.8406 |

![Confusion Matrix](/images/confmatrix_bert256.png)

* Brief escription:

### For Frozen RoBERTa with a truncation limit of 512:

#### On Average:

| accuracy | macro-F1 | precision | recall |
| --- | --- | --- | --- |
| 0.9153 | 0.9158 | 0.9208   | 0.9153 |

#### Per-Class:

| | precision | recall | F1-score |
| --- | --- | --- | --- |
| human | 0.9526   | 0.8440   | 0.8950 |
| ai_generated | 0.9776   | 0.9600   | 0.9687 |
| ai_refined | 0.8322   | 0.9420 |   0.8837  |

![Confusion Matrix](images/confmatrix_bert512.png)

* Brief escription:

Comparison between 3 models, describe strengths and weaknesses of each. Explain possible reasons.

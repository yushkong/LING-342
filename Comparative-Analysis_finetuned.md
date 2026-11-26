# Quantitative Analysis
we looked at accuracy, precision, recall, and Macro-F1. For each class, we looked at precision, recall, and F1 as well. Lastly, a confusion matrix is included.

* **Accuracy** was selected as a big-picture measure of performance.
* **Macro-F1** was selected as an overview of per-class F1 scores for a balanced look at how the models perform in terms of precision and recall. **F1** was also calculated for each class for a more individual look at what classes the models perform better at.
* **Precision and recall** were selected to get a better idea of what types of error each model tends to produce. These were looked at both on average and for individual classes for a closer look.
* **Confusion matrices** were added to give a visual representation of the types of errors the models tend towards.


### For the non-truncated TF-IDF Logistic Regression model:

#### On Average:

| accuracy | macro-F1 | precision | recall |
| --- | --- | --- | --- |
| 0.9587 | 0.9586 | 0.9600 | 0.9587 |

#### Per-Class:

| | precision | recall | F1-score |
| --- | --- | --- | --- |
|  human | 0.9870 | 0.9120 | 0.9480 |
| ai_generated | 0.9766 | 1.000 | 0.9881 |
| ai_refined | 0.9163 | 0.9640 | 0.9396 |

#### Comparative table: 

| | accuracy | macro-F1 | precision | recall |
| --- | --- | --- | --- | --- |
| Non-truncated TF-IDF | 0.8657 | 0.8637 | 0.8656 | 0.8657 |
| Truncated TF-IDF | 0.7947 | 0.7961 | 0.8072 | 0.7947 |
| Frozen RoBERTa (256) | 0.8820 | 0.8837 | 0.8937 | 0.8820 |
| Frozen RoBERTa (512) | 0.9153 | 0.9158 | 0.9208   | 0.9153 |
| Fine-tuned RoBERTa (512) | 0.9587 | 0.9586 | 0.9600 | 0.9587 |


#### Confusion Matrix:

![Confusion Matrix](/images/confmatrix_bertfnetuned.png)

#### Notes
* Overall, this model outperformed all four of our baseline models by a significant margin. Between the fine-tuned RoBERTa and the previously best model (frozen RoBERTa with 512 limit), accuracy improved by 4.34%, macro-F1 improved by 4.28%, precision improved by 3.92%, and recall improved by 4.34%. This suggests that fine-tuning was an effective way to improve the performance of the model.
* more comparative differences for per-class 
* Notably, the fine-tuned model has a recall of 100% for AI-generated samples. Alongside a high precision of 97.66% for the AI-generated class, this is extremely promising performance for detecting AI-generated text, although it also suggests that the model is more prone to overgeneralizing rather than undergeneralizing AI-generated texts.


# Qualitative Analysis
For qualitative analysis, we are interested in comparing examples that were classified incorrectly for our baseline models, which were then fixed in the new model, and examples that were classed correctly for our baseline models but are now classed incorrectly for our fine-tuned model. 

#### Examples that got fixed

#### Examples that got worse

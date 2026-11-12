### Notes
1. We use two approaches:
* Lexical vs. Contextual
* TF-IDF baseline: converts text into TF-IDF-weighted lexical features, followed by Logistic Regression.
* Frozen RoBERTa: extracts contextual representations from a pretrained RoBERTa model without updating its parameters, followed by a trained classifier.

2. BERT has a 512-token limit, so the input to RoBERTa needs to be truncated.
* Frozen RoBERTa's general accuracy increased when the truncation limit doubled from 256 to 512.

3. TF-IDF doesn't have a token limit.

4. The Result
| Approach                   | Test size | Accuracy | Macro-F1 |
| -------------------------- | --------- | -------- | -------- |
| TF-IDF, 256 tokens         | 1,500     | 79.47%   | 79.61%   |
| Frozen RoBERTa, 256 tokens | 1,500     | 88.20%   | 88.37%   |
| TF-IDF, untruncated        | 6,000     | 86.57%   | 86.37%   |
| Frozen RoBERTa, 512 tokens | 1,500     | 92.73%   | 92.70%   |

5. Given the prediction samples, a possible bias in the database is that wiki-domain data with ai participation often include markdown symbols and extra title, which is not common in human samples. However, these models generally performed better in `wiki` classification than `academic`.




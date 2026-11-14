# Qualitative Analysis

In the codebases for each model, examples were generated for correct and incorrect predictions. Each example was analyzed, and representative ones were selected for discussion below. Due to the length of text, we will not include the full text of these examples here, but we will use other representative information to describe them.

### Bias in Dataset
In the prediction samples, we observe that suggesting patterns such as headings, bullet points and Markdown formatting are common in `wiki` domain data with AI involvement, but not in human examples. This would probably allow the classifier learn to identify the formatting conventions rather than the underlying linguistic characteristics of texts. However, accuracy in `academic` domain is generally higher than `wiki` domain in all experiment runs, regarding that these patterns are not observed in `academic`.

### Non-truncated TF-IDF:

#### Correct examples

1. **AI-generated (Pair 38141):** AI-generated passage about Hammam Sousse. It presents historical information in a polished, chronological narrative, with smooth transitions between periods and consistently formal language. Phrases such as "a rich history that stretches back to ancient times" and "a testament to Tunisia's diverse and layered past" might be considered descriptive elaboration beyond basic factual reporting that is indicative of AI generation. 

2. **AI-refined (Pair 109719):** AI-refined passage discussing Hume's causality theory. It retains specialized academic vocabulary, citations, and philosophical arguments while presenting the material in relatively clear, organized language. The specialized vocabulary may help distinguish AI-refined text from original human writing, while the organization might help distinguish it from fully AI-generated passages.

**3. Human (Pair 111373):** Human-written passage discussing medieval chroniclers. Unlike the other examples, it contains irregular sentence structures, unconventional punctuation, and formatting artifacts such as broken words ("in- formation" and "nar- rative"). It also includes embedded footnote numbers and citations that interrupt the prose. These features may provide lexical or structural signals that distinguish the passage from the more consistently formatted AI-generated and AI-refined texts.

#### Incorrect examples

1. **Human, classified as AI-generated (Pair 111577):** A human-written academic passage discussing Ricoeur's concept of the subject of rights. The text uses formal argumentation and specialized vocabulary. This suggests that academic writing that is less stylized may share linguistic characteristics with AI-generated text, making it difficult for the model to distinguish between them.

2. **AI-generated, classified as Human (Pair 38968):** An AI-generated passage describing the responsibilities of the WHO Director-General. Its neutral, factual tone and conventional encyclopedic structure might resemble human-authored reference material that is also meant to be formal, potentially contributing to the misclassification. This and the first example illustrate what might be considered ambiguous features.

3. **AI-refined, classified as AI-generated (Pair 110813):** An AI-refined academic passage discussing literary canons. The passage contains elaborate phrasing and extensive reformulation, including expressions such as "intricate gnoseological and epistemological dilemma." AI rewriting may introduce stylistic patterns similar to fully AI-generated text, so this type of confusion can be expected.

4. **AI-refined, classified as Human (Pair 38894):** An AI-refined biographical passage about Konrad von Wangenheim. The passage is concise and fact-heavy, with relatively little stylistic elaboration. It may have retained enough characteristics of conventional human-authored writing to be mistaken for the human class.

#### Overall Observations

These examples illustrate that the boundaries between human-written, AI-generated, and AI-refined text are not always linguistically distinct. Formal academic writing can resemble AI-generated text, while AI-refined passages may either retain human-like characteristics or exhibit extensive AI-style rewriting.

For future improvements, we could investigate stylistic features beyond word frequency, fine-tune contextual models such as RoBERTa, and compare original human passages with their AI-refined counterparts to better understand how refinement changes detectable writing patterns.

### Truncated TF-IDF:

#### Correct Classifications

1. **AI-generated (Pair 109663):** AI-generated academic passage discussing cyber media and Derrida's concept of "pharmakon". It uses a structured explanation with explicit transitions such as "On one hand" and "On the other hand," alongside repeated elaboration of the central concept. These relatively predictable explanatory patterns may have contributed to the correct classification.

2. **AI-refined (Pair 37656):** AI-refined biographical passage about architect James Edward Ware. It presents factual information through polished, varied phrasing, including expressions such as "gained renown" and "earned acclaim." The combination of factual content and stylistic elaboration may help distinguish AI refinement from unmodified reference writing.

3. **Human (Pair 37691):** Human-written passage about Abu Nasr Husayn II. Unlike the other examples, it discusses conflicting historical evidence and uncertainties, referring to discrepancies between historical accounts and coinage records. Its specialized terminology and detailed source comparisons may provide distinguishing features, although these characteristics are not exclusive to human writing.

#### Incorrect Classifications

1. **AI-generated, classified as AI-refined (Pair 37614):** An AI-generated passage about the 40th Walker Cup Match. It contains descriptive and embellished expressions such as "eagerly anticipated," "nail-biting finish," and "prestigious biennial contest." This suggests that stylistically elaborate AI-generated writing may be difficult to distinguish from text that has undergone AI refinement.

2. **AI-refined, classified as Human (Pair 37526):** An AI-refined biography of Carlo Francesco Cogrossi. The passage is concise and primarily factual, listing dates, historical events, and professional achievements with relatively little elaboration. Its similarity to conventional encyclopedic writing may have contributed to the misclassification.

3. **Human, classified as AI-generated (Pair 110701):** A human-written academic passage about Chinese Indonesians during the New Order era. It uses formal academic language, historical context, and citations, with a clear progression of ideas. This illustrates how structured human-written academic prose may resemble AI-generated explanations.

4. **Human, classified as AI-refined (Pair 38813):** A human-written encyclopedic entry about Caesarea. The passage consists largely of geographical names and factual descriptions arranged into categories. Interestingly, the corresponding AI-generated passage from the same pair was also classified as AI-refined. This suggests that the model may be responding to shared topical vocabulary or organizational features rather than reliably distinguishing the writing process.

#### Overall Observations

These examples suggest that the model has difficulty distinguishing classes when their linguistic characteristics overlap. AI-generated passages may resemble refined writing when they contain elaborate phrasing, while AI-refined passages may be mistaken for human writing when they preserve a straightforward factual style. Similarly, formal and well-structured human writing may be incorrectly associated with AI involvement.

Pair 38813 is especially interesting because both the human-written and AI-generated versions were assigned the same incorrect label. This raises the possibility that shared content and structure influence the classifier's decisions.

We could investigate whether the model relies too heavily on topical vocabulary by comparing predictions across paired passages. We could also explore character-level features, stylistic measurements, and fine-tuning contextual representations to improve distinctions between the three classes.


### Frozen RoBERTa with a truncation limit of 256:

#### Correct examples
1. **AI-generated (Pair 111707):** AI-generated academic passage about vehicle communication systems. The passage follows a structured explanatory format. Its consistently polished language and organized presentation may have contributed to the correct prediction.

2. **AI-refined (Pair 38313):** An AI-refined passage about Ted Hughes's Tales from Ovid. It combines neutral phrasing with more elaborate phrasing, including descriptions such as "poetic masterpiece" and "garnering critical acclaim." This stylistic embellishment may be a useful indicator of AI refinement.

3. **Human (Pair 36868):** Human-written biography of Irene Siegel. The passage contains relatively straightforward factual descriptions alongside less polished phrasing, such as "Her name was Irene Yarovich at birth." Its relatively uneven sentence structures may help distinguish it from the more consistently polished AI-generated and AI-refined passages.

#### Incorrect Classifications

1. **Human, classified as AI-generated (Pair 36953):** A human-written passage about military forward-basing. It provides a systematic explanation of the concept, followed by its advantages, risks, and examples. This organized structure resembles common AI-generated explanatory writing, potentially contributing to the misclassification.

2. **AI-refined, classified as AI-generated (Pair 36953):** AI-refined version of the same forward-basing passage from the first incorrect example. Both versions retain similar content and organization despite differences in wording. This suggests that the classifier may rely partly on topical features.

3. **AI-generated, classified Human (Pair 38968):** AI-generated passage describing the WHO Director-General. Its factual, neutral tone resembles conventional encyclopedic writing, potentially making it difficult to distinguish from human-authored reference material.

4. **AI-refined, Human (Pair 37505):** AI-refined biography of painter Charles Louis Müller. The passage contains factual statements, dates, and lists of works, with little stylistic elaboration. Its relatively unpolished format may have made it more similar to the human-written examples in the dataset.

#### Overall Observations

These examples suggest that the model may associate polished, systematically organized writing with AI generation, while more straightforward or irregularly structured passages are sometimes classified as human-written. However, these patterns are not consistent enough to reliably distinguish the three classes.

Pair 36953 is informative because both the human-written and AI-refined passages were incorrectly classified as AI-generated. Their similar content and organization raise the possibility that the classifier relies partly on topical or structural similarities rather than features specific to the writing process.

For future improvements, we could investigate the effects of text structure and vocabulary through paired comparisons, experiment with additional stylistic features, and evaluate whether longer input sequences or fine-tuned contextual representations improve distinctions between the classes.


### Frozen RoBERTa with a truncation limit of 512:

#### Correct examples
1. **AI-generated (Pair 36860):** AI-generated passage explaining cashback websites. The passage uses a highly structured explanatory format, with sections describing how cashback websites work and their additional features. It also contains organized lists and polished transitions, which may have contributed to its identification as AI-generated.

2. **AI-refined (Pair 111402):** AI-refined academic passage discussing Hegel's philosophy. It preserves specialized philosophical terminology and citations while using explanatory transitions such as "Put differently" to clarify complex ideas. This combination of academic content and reformulation may help distinguish AI-refined text.

3. **Human (Pair 111382):** Human-written philosophical passage discussing historical injustices. The text contains argumentative language, direct engagement with other scholars, and formatting irregularities such as broken words and embedded page headers. These features may distinguish it from the more consistently polished AI-generated passages, although some irregularities likely result from document extraction.

#### Incorrect Classifications

1. **Human, classified as AI-generated (Pair 36953):** A human-written passage about military forward-basing. It provides a systematic explanation of the concept, followed by its advantages, risks, and practical examples. Its organized structure may resemble AI-generated explanatory writing.

2. **AI-refined, classified as AI-generated (Pair 36953):** AI-refined version of the same forward-basing passage from the first incorrect example was also classified as AI-generated. Both versions retain similar information and organization despite differences in wording. This suggests that the classifier may rely partly on shared content and structural features rather than distinguishing the writing process.

3. **AI-generated, classified as Human (Pair 38813):** AI-generated passage about places named Caesarea. The passage primarily consists of factual descriptions and geographical lists, resembling conventional encyclopedic content. Its relatively straightforward informational structure may have contributed to the misclassification.

4. **AI-refined, classified as Human (Pair 38999):** AI-refined passage about the film An Ethics Lesson. It preserves much of the original encyclopedia-style structure, including plot summaries, cast lists, and categorical information. This suggests that AI refinement may be difficult to detect when the original formatting and factual content remain largely unchanged.

#### Overall Observations

These examples suggest that the model struggles when different classes share similar vocabulary, structure, and writing styles. Highly organized human-written passages may resemble AI-generated explanations, while AI-refined passages that preserve their original structure may be mistaken for human writing.

Pair 36953 is particularly informative because both the original human-written text and its AI-refined counterpart were classified as AI-generated. This raises the possibility that the model relies partly on shared topical and structural characteristics rather than features specific to authorship.

The correctly classified human example also contains formatting artifacts, suggesting that source-document formatting may influence classification. This warrants further investigation, as such features may not generalize to cleaner real-world text.

For future improvements, we could compare predictions across paired passages, normalize formatting artifacts, and investigate whether additional stylistic or contextual features improve distinctions between the three classes.


### Comparative Observations

Across all four models, the most common difficulty was distinguishing AI-refined text from human-written or fully AI-generated text. However, their error patterns reveal differences in how each model approaches classification.

* **Non-truncated TF-IDF:** Performed well at distinguishing human-written from fully AI-generated text but struggled with AI-refined passages. Errors often involved formal academic writing or factual encyclopedic content, suggesting that word-frequency features alone may not adequately distinguish AI refinement.

* **Truncated TF-IDF:** Greater confusion between AI-generated and AI-refined text. Removing portions of the input may have eliminated useful lexical information, making the model more reliant on limited vocabulary and local patterns.

* **Frozen RoBERTa (256 tokens):** Generally handled AI-refined text better than TF-IDF, but sometimes classified both human-written and AI-refined versions of the same passage as AI-generated (e.g., pair 36953). This suggests that contextual embeddings may still be influenced by shared content and structure.

* **Frozen RoBERTa (512 tokens):** Achieved the strongest overall performance and improved recognition of AI-generated and AI-refined text. However, it continued to misclassify some human-written passages as AI-generated, including pair 36953. Longer contextual representations appear beneficial, but do not fully resolve the overlap between classes.

In all, the results suggest that contextual representations outperform purely lexical features, while longer input sequences generally improve classification performance. Nevertheless, all models remain sensitive to similarities in topic, writing style, and structure across classes. Several correctly classified examples also contained formatting or generation artifacts, raising the possibility that models learn dataset-specific cues rather than authorship characteristics.

Future improvements could include fine-tuning RoBERTa, normalizing formatting artifacts, and systematically comparing predictions across paired passages to investigate whether models rely on content rather than writing origin.
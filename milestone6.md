# Qualitative Analysis

In the codebases for each model, examples were generated for correct and incorrect predictions. Each example was analyzed, and representative ones were selected for discussion below. Due to the length of text, we will not include the full text of these examples here, but we will use other representative information to describe them.

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

### Correct Classifications

1. **AI-generated (Pair 109663):** AI-generated academic passage discussing cyber media and Derrida's concept of "pharmakon". It uses a structured explanation with explicit transitions such as "On one hand" and "On the other hand," alongside repeated elaboration of the central concept. These relatively predictable explanatory patterns may have contributed to the correct classification.

2. **AI-refined (Pair 37656):** AI-refined biographical passage about architect James Edward Ware. It presents factual information through polished, varied phrasing, including expressions such as "gained renown" and "earned acclaim." The combination of factual content and stylistic elaboration may help distinguish AI refinement from unmodified reference writing.

3. **Human (Pair 37691):** Human-written passage about Abu Nasr Husayn II. Unlike the other examples, it discusses conflicting historical evidence and uncertainties, referring to discrepancies between historical accounts and coinage records. Its specialized terminology and detailed source comparisons may provide distinguishing features, although these characteristics are not exclusive to human writing.

### Incorrect Classifications

1. **AI-generated, classified as AI-refined (Pair 37614):** An AI-generated passage about the 40th Walker Cup Match was classified as AI-refined. It contains descriptive and embellished expressions such as "eagerly anticipated," "nail-biting finish," and "prestigious biennial contest." This suggests that stylistically elaborate AI-generated writing may be difficult to distinguish from text that has undergone AI refinement.

2. **AI-refined, classified as Human (Pair 37526):** An AI-refined biography of Carlo Francesco Cogrossi was classified as human-written. The passage is concise and primarily factual, listing dates, historical events, and professional achievements with relatively little elaboration. Its similarity to conventional encyclopedic writing may have contributed to the misclassification.

3. **Human, classified as AI-generated (Pair 110701):** A human-written academic passage about Chinese Indonesians during the New Order era was classified as AI-generated. It uses formal academic language, historical context, and citations, with a clear progression of ideas. This illustrates how structured human-written academic prose may resemble AI-generated explanations.

4. **Human, classified as AI-refined (Pair 38813):** A human-written encyclopedic entry about Caesarea was classified as AI-refined. The passage consists largely of geographical names and factual descriptions arranged into categories. Interestingly, the corresponding AI-generated passage from the same pair was also classified as AI-refined. This suggests that the model may be responding to shared topical vocabulary or organizational features rather than reliably distinguishing the writing process.

### Overall Observations

The examples suggest that the model has difficulty distinguishing classes when their linguistic characteristics overlap. AI-generated passages may resemble refined writing when they contain elaborate phrasing, while AI-refined passages may be mistaken for human writing when they preserve a straightforward factual style. Similarly, formal and well-structured human writing may be incorrectly associated with AI involvement.

Pair 38813 is especially interesting because both the human-written and AI-generated versions were assigned the same incorrect label. This raises the possibility that shared content and structure influence the classifier's decisions.

We could investigate whether the model relies too heavily on topical vocabulary by comparing predictions across paired passages. We could also explore character-level features, stylistic measurements, and fine-tuning contextual representations to improve distinctions between the three classes.


### Frozen RoBERTa with a truncation limit of 256:

#### Correct examples
#### Inorrect examples



### Frozen RoBERTa with a truncation limit of 512:

#### Correct examples
#### Inorrect examples

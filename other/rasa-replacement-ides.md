# Non-LLM Intent Classification: Initial Analysis

This document outlines alternatives to LLM-based intent classification for chatbot logic. These methods are CPU-friendly, low-cost, and suitable when 
GPU usage or cloud API costs are a concern.

---

## Summary

| Method                        | Training Needed | Handles Semantics | Speed (CPU) | Flexibility | Maintenance | Best Use Case |
|------------------------------|------------------|-------------------|-------------|-------------|-------------|----------------|
| scikit-learn + TF-IDF        | ✅ Yes           | ❌ Limited         | ⚡⚡⚡ Fast    | Medium      | Low         | Structured intent routing |
| spaCy Rule Matching          | ❌ No            | ❌ None            | ⚡⚡⚡ Very Fast | Low         | High (rules) | Compliance, fixed commands |
| Sentence Transformers + kNN  | ❌ No            | ✅ Strong          | ⚡ Medium    | High        | Medium      | Semantic bots, small datasets |

---

##  Method 1: scikit-learn + TF-IDF (Classic ML)

### Pros:
- Extremely fast inference
- Simple and transparent
- Easy to deploy and maintain

### Cons:
- Requires training with labeled data
- Poor semantic understanding
- Needs many examples to generalize

###  Example:
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample dataset
texts = [
    "i need a new id card",
    "apply for national id",
    "renew my identity document",
    "change my id pin",
    "reset pin code for id",
    "update my card pin",
    "talk to a representative",
    "i want to speak with an agent"
]
labels = [
    "request_id_card",
    "request_id_card",
    "request_id_card",
    "change_id_pin",
    "change_id_pin",
    "change_id_pin",
    "escalate_to_agent",
    "escalate_to_agent"
]

# Train the classifier
vec = TfidfVectorizer()
X = vec.fit_transform(texts)
clf = LogisticRegression()
clf.fit(X, labels)

# Test it
query = vec.transform(["i want to update my pin"])
print(clf.predict(query))  # -> "change_id_pin"

```

## Method 2: spaCy Rule-Based Matching
### Pros:

- No training required
- Deterministic and explainable
- Fastest runtime

### Cons:

- Doesn't handle language variation
- Requires manual pattern writing
- Low flexibility

### Example:

```python
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

# Add a rule for ID card request
matcher.add("REQUEST_ID_CARD", [[
    {"LOWER": {"IN": ["need", "apply", "renew"]}},
    {"LOWER": {"IN": ["id", "identity"]}},
    {"LOWER": "card"}
]])

# Add a rule for changing PIN
matcher.add("CHANGE_ID_PIN", [[
    {"LOWER": {"IN": ["change", "reset", "update"]}},
    {"LOWER": "pin"},
    {"LOWER": "code", "OP": "?"}
]])

doc = nlp("i need to renew my identity card")
matches = matcher(doc)
for match_id, start, end in matches:
    print(nlp.vocab.strings[match_id])  # -> REQUEST_ID_CARD

```

## Method 3: Sentence Transformers + kNN (Semantic Search)
### Pros:

- Handles semantic variation and paraphrasing
- No training required
- Works well with few examples

### Cons:

- Slightly slower on CPU (~100–300ms)
- Requires downloading models (~300MB)
- May be imprecise with short/ambiguous input

### Example:

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

# Few-shot examples
intents = {
    "request_id_card": [
        "i need an id card",
        "renew my identity document",
        "apply for national id"
    ],
    "change_id_pin": [
        "reset my id pin",
        "change the pin code on my card",
        "update id pin"
    ],
    "escalate_to_agent": [
        "i want to talk to someone",
        "speak to an agent",
        "connect me with a representative"
    ]
}

# Embed intent examples
intent_embeddings = {
    intent: model.encode(samples, convert_to_tensor=True)
    for intent, samples in intents.items()
}

# Test query
query_vec = model.encode("how do I reset the PIN on my ID card?", convert_to_tensor=True)

# Compare using cosine similarity
scores = {
    intent: max(util.cos_sim(query_vec, embs)).item()
    for intent, embs in intent_embeddings.items()
}

print(max(scores, key=scores.get))  # -> change_id_pin

```


## Hybrid Strategy

### Combine the strengths of all methods:

- spaCy Rule Matching: For critical/high-confidence patterns.
- Sentence Transformers: Fallback for natural language inputs.
- scikit-learn (Optional): For quick training-based workflows.

## Final Thoughts

If we want a fast, accurate, low-cost, CPU-only pipeline for intent detection:

- Use Sentence Transformers + kNN
- Add spaCy rules for critical commands
- Wrap in a simple API (FastAPI) for production use (needs discussion if it fits into general archidecture)

This gives us the flexibility of semantic search and the speed of rule-based classification — with zero dependency on GPUs or expensive LLM APIs.

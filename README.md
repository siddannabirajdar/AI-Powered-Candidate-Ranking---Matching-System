# AI-Powered Candidate Ranking & Matching System

---

## Problem Statement

Build an intelligent AI-powered recruitment system capable of ranking candidates for a given Job Description (JD) using semantic understanding, career signals, behavioral indicators, and explainable reasoning.

The solution must move beyond traditional keyword matching and identify candidates who genuinely align with the role requirements.

---

## Solution Overview

Our solution combines semantic retrieval with multi-signal ranking to identify the most relevant candidates.

The system:

1. Understands the Job Description using transformer embeddings.
2. Retrieves relevant candidates using semantic similarity.
3. Evaluates candidates across multiple dimensions:

   * Career relevance
   * Retrieval/Search expertise
   * JD intent alignment
   * Achievement evidence
   * Behavioral signals
4. Produces a final ranked list.
5. Generates recruiter-friendly explanations for every shortlisted candidate.

---

## Architecture

```text
Job Description
        │
        ▼
BGE Embedding Model
        │
        ▼
JD Embedding
        │
        ▼

Candidate Profiles
        │
        ▼
Candidate Embeddings
        │
        ▼

Cosine Similarity Retrieval
        │
        ▼

Multi-Signal Ranking Engine

 ├── Career Score
 ├── Retrieval Score
 ├── JD Intent Score
 ├── Achievement Score
 └── Behavior Score

        │
        ▼

Final Candidate Ranking
        │
        ▼

Evidence Extraction
        │
        ▼

Reasoning Generation
        │
        ▼

Top 100 Candidates
```

---

## Ranking Methodology

### 1. Semantic Similarity

* BAAI/bge-base-en-v1.5 embeddings
* Cosine similarity between JD and candidate profile

### 2. Career Score

Evaluates:

* Relevant AI/ML roles
* Search and recommendation experience
* Product company exposure
* Preferred experience range
* Negative or unrelated roles

### 3. Retrieval Experience Score

Detects expertise in:

* Search
* Retrieval
* Ranking
* Recommendation Systems
* Vector Search
* FAISS
* Pinecone
* Elasticsearch
* RAG

### 4. JD Intent Score

Measures alignment with:

* Retrieval systems
* Evaluation frameworks
* Production AI systems
* Modern AI techniques

### 5. Achievement Score

Identifies:

* NDCG
* MRR
* MAP
* Latency improvements
* A/B testing
* Production deployments
* Quantifiable impact

### 6. Behavior Score

Uses:

* Open-to-work status
* Activity recency
* Recruiter responsiveness
* Interview completion rate
* Verification status
* GitHub activity
* Profile completeness

---

## Explainability

Every shortlisted candidate receives an explanation generated from actual profile evidence.

Example:

> Lead AI Engineer with 6.7 years of experience at Razorpay. Key evidence: Designed the offline evaluation framework from scratch — NDCG, MRR, recall@K calibrated against online A/B engagement metrics. Strong fit for retrieval, ranking and production AI systems.

No hallucinated information is generated. All reasoning is grounded in candidate profile data.

---

## Technologies Used

* Python
* Sentence Transformers
* BAAI/bge-base-en-v1.5
* Scikit-Learn
* NumPy
* Pandas
* Cosine Similarity
* GitHub

---

## Repository Structure

```text
AI_Recruiter_Hackathon/

├── data/
├── docs/
├── src/
├── candidate_ids.npy
├── candidate_embeddings.npy
├── submission.csv
├── requirements.txt
└── README.md
```

---

## How To Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate rankings:

```bash
python src/main.py
```

Generate submission file:

```bash
python src/submission_generator.py
```

Output:

```text
submission.csv
```

containing:

* rank
* candidate_id
* score
* reasoning

---

## Deliverables

* Source Code
* Ranked Top 100 Candidates
* Explainable Reasoning
* Submission CSV
* Presentation Deck

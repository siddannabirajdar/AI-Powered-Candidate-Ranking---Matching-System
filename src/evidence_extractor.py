IMPORTANT_KEYWORDS = {

    "candidate-jd": 5,
    "candidate matching": 5,

    "retrieval": 3,
    "ranking": 3,
    "recommendation": 3,

    "ndcg": 5,
    "mrr": 4,
    "map": 4,

    "a/b": 4,
    "evaluation": 4,

    "embeddings": 3,
    "vector search": 3,

    "faiss": 4,
    "pinecone": 4,
    "qdrant": 4,

    "llm": 3,
    "rag": 4,

    "real users": 4,
    "latency": 4,

    "production": 3,
    "deployed": 3,

    "engagement": 5,
    "queries": 3,
    "million": 4
}

import re


def extract_best_evidence(candidate):

    best_sentence = ""

    best_score = -1

    for job in candidate.get(
        "career_history",
        []
    ):

        description = job.get(
            "description",
            ""
        )

        sentences = description.split(
            "."
        )

        for sentence in sentences:

            text = sentence.lower()

            score = 0

            for keyword, weight in (
                IMPORTANT_KEYWORDS.items()
            ):

                if keyword in text:

                    score += weight

            # reward numbers

            numbers = re.findall(
                r"\d+",
                text
            )

            score += min(
                len(numbers),
                5
            )

            # reward impact words

            impact_words = [

                "improved",
                "increased",
                "reduced",
                "optimized",
                "scaled",
                "served",
                "deployed",
                "migrated"
            ]

            for word in impact_words:

                if word in text:

                    score += 2

            if score > best_score:

                best_score = score

                best_sentence = (
                    sentence.strip()
                )

    return best_sentence
RETRIEVAL_KEYWORDS = {

    "retrieval": 15,
    "information retrieval": 20,

    "search": 12,
    "semantic search": 20,
    "hybrid search": 25,

    "ranking": 15,
    "reranking": 20,

    "recommendation": 15,
    "recommendation system": 25,

    "candidate matching": 25,
    "matching": 10,

    "embedding": 15,
    "embeddings": 15,

    "vector search": 25,
    "vector database": 25,

    "faiss": 25,
    "pinecone": 25,
    "qdrant": 25,
    "milvus": 25,

    "elasticsearch": 20,
    "opensearch": 20,

    "llm": 10,
    "rag": 15,

    "ndcg": 20,
    "mrr": 20,
    "map": 20
}


def retrieval_experience_score(candidate):

    score = 0

    found_keywords = set()

    profile = candidate.get(
        "profile",
        {}
    )

    text_parts = [

        profile.get(
            "headline",
            ""
        ),

        profile.get(
            "summary",
            ""
        )
    ]

    for job in candidate.get(
        "career_history",
        []
    ):

        text_parts.append(

            job.get(
                "title",
                ""
            )
        )

        text_parts.append(

            job.get(
                "description",
                ""
            )
        )

    text = " ".join(
        text_parts
    ).lower()

    for keyword, value in (
        RETRIEVAL_KEYWORDS.items()
    ):

        if (
            keyword in text
            and keyword not in found_keywords
        ):

            score += value

            found_keywords.add(
                keyword
            )

    return min(
        score,
        60
    )
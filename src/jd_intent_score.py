INTENT_GROUPS = {

    "retrieval_systems": [

        "retrieval",
        "search",
        "semantic search",
        "hybrid retrieval",
        "vector search",

        "candidate matching",

        "recommendation system",

        "ranking pipeline"
    ],

    "evaluation": [

        "ndcg",
        "mrr",
        "map",

        "ab test",
        "a/b test",

        "evaluation framework",

        "offline evaluation",

        "online evaluation"
    ],

    "production": [

        "production",
        "deployed",

        "latency",

        "real users",

        "million",

        "serving",

        "kubernetes",

        "inference"
    ],

    "modern_ai": [

        "llm",
        "rag",

        "fine-tuning",

        "qlora",

        "lora",

        "embeddings",

        "reranking"
    ]
}


def jd_intent_score(candidate):

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

    score = 0

    for keywords in (
        INTENT_GROUPS.values()
    ):

        matches = 0

        for keyword in keywords:

            if keyword in text:

                matches += 1

        if matches >= 4:

            score += 15

        elif matches >= 2:

            score += 8

        elif matches >= 1:

            score += 3

    return min(
        score,
        40
    )
import re


IMPACT_WORDS = [

    "improved",
    "increased",
    "reduced",
    "optimized",

    "scaled",

    "deployed",

    "launched",

    "production"
]


def achievement_score(candidate):

    score = 0

    text_parts = []

    for job in candidate.get(
        "career_history",
        []
    ):

        text_parts.append(

            job.get(
                "description",
                ""
            )
        )

    text = " ".join(
        text_parts
    ).lower()

    # Impact signals

    for word in IMPACT_WORDS:

        if word in text:

            score += 5

    # Ranking metrics

    if "ndcg" in text:

        score += 10

    if "mrr" in text:

        score += 10

    if "map" in text:

        score += 10

    # Scale indicators

    if "100m" in text:

        score += 20

    elif "50m" in text:

        score += 15

    elif "10m" in text:

        score += 10

    elif "million" in text:

        score += 5

    # Latency optimization

    if "latency" in text:

        score += 10

    # Experimentation

    if (
        "a/b" in text
        or "ab test" in text
    ):

        score += 10

    # Quantitative evidence

    numbers = re.findall(
        r"\d+",
        text
    )

    score += min(
        len(numbers),
        10
    )

    return min(
        score,
        50
    )
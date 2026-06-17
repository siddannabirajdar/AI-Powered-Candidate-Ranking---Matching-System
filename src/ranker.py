import json
import numpy as np

from sklearn.metrics.pairwise import (
    cosine_similarity
)

from embedder import get_embedding
from career_scorer_v2 import career_score
from behavior_scorer import behavior_score
from retrieval_experience_score import (
    retrieval_experience_score
)
from jd_intent_score import (
    jd_intent_score
)
from achievement_score import (
    achievement_score
)


def load_job_description():

    with open(
        "docs/job_description.txt",
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()


def load_candidate_data():

    candidate_ids = np.load(
        "candidate_ids.npy",
        allow_pickle=True
    )

    candidate_embeddings = np.load(
        "candidate_embeddings.npy"
    )

    candidate_lookup = {}

    with open(
        "data/candidates.jsonl",
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            candidate = json.loads(
                line
            )

            candidate_lookup[
                candidate["candidate_id"]
            ] = candidate

    return (
        candidate_ids,
        candidate_embeddings,
        candidate_lookup
    )


def rank_candidates():

    jd_text = (
        load_job_description()
    )

    (
        candidate_ids,
        candidate_embeddings,
        candidate_lookup
    ) = load_candidate_data()

    print(
        "\nGenerating JD Embedding..."
    )

    jd_embedding = get_embedding(
        jd_text
    )

    print(
        "Calculating Similarities..."
    )

    similarities = cosine_similarity(
        [jd_embedding],
        candidate_embeddings
    )[0]

    results = []

    for idx, candidate_id in enumerate(
        candidate_ids
    ):

        candidate = candidate_lookup[
            candidate_id
        ]

        semantic_score = (
            similarities[idx] * 100
        )

        career = career_score(
            candidate
        )

        retrieval = (
            retrieval_experience_score(
                candidate
            )
        )

        intent = jd_intent_score(
            candidate
        )

        achievement = (
            achievement_score(
                candidate
            )
        )

        behavior = behavior_score(
            candidate[
                "redrob_signals"
            ],
            ""
        )

        # Final ranking score combines:
        # semantic relevance
        # retrieval expertise
        # JD intent alignment
        # achievement signals
        # career quality
        # behavioral signals

        final_score = (

            semantic_score * 2.0

            + retrieval

            + intent

            + achievement

            + (career * 0.3)

            + (behavior * 0.7)

        )

        results.append({

            "candidate_id":
            candidate_id,

            "candidate":
            candidate,

            "semantic":
            semantic_score,

            "retrieval":
            retrieval,

            "intent":
            intent,

            "achievement":
            achievement,

            "career":
            career,

            "behavior":
            behavior,

            "score":
            final_score
        })

    results.sort(

        key=lambda x: x["score"],

        reverse=True
    )

    return results
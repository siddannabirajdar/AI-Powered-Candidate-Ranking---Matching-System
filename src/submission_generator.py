import csv

from ranker import rank_candidates
from reasoning_generator import (
    generate_reasoning
)


def generate_submission():

    results = rank_candidates()

    with open(
        "submission.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            "rank",
            "candidate_id",
            "score",
            "reasoning"
        ])

        for rank, result in enumerate(
            results[:100],
            start=1
        ):

            candidate = result[
                "candidate"
            ]

            reasoning = (
                generate_reasoning(
                    candidate
                )
            )

            writer.writerow([
                rank,
                result["candidate_id"],
                round(
                    result["score"],
                    2
                ),
                reasoning
            ])

    print(
        "submission.csv generated"
    )


if __name__ == "__main__":

    generate_submission()
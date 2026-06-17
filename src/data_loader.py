import json


def load_sample_candidates(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def load_jsonl_candidates(path):

    candidates = []

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            candidates.append(
                json.loads(line)
            )

    return candidates


if __name__ == "__main__":

    candidates = load_jsonl_candidates(
        "data/candidates.jsonl"
    )

    print(
        "Total Candidates:",
        len(candidates)
    )

    print(
        "First Candidate:",
        candidates[0]["candidate_id"]
    )
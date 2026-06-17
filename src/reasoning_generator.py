from evidence_extractor import (
    extract_best_evidence
)


def generate_reasoning(candidate):

    profile = candidate.get(
        "profile",
        {}
    )

    title = profile.get(
        "current_title",
        ""
    )

    company = profile.get(
        "current_company",
        ""
    )

    years = profile.get(
        "years_of_experience",
        0
    )

    evidence = extract_best_evidence(
        candidate
    )

    reason = (

        f"{title} with "

        f"{years} years of experience "

        f"at {company}. "
    )

    if evidence:

        reason += (

            "Key evidence: "

            + evidence

            + ". "
        )

    reason += (

        "Strong fit for Redrob's Senior AI Engineer role due to "

        "hands-on experience with retrieval, ranking, "

        "candidate matching, evaluation frameworks and "

        "production AI systems."
    )

    return reason
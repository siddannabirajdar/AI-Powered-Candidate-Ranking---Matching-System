def build_candidate_text(candidate):

    profile = candidate.get(
        "profile",
        {}
    )

    text_parts = []

    # Profile

    text_parts.append(
        f"Headline: {profile.get('headline','')}"
    )

    text_parts.append(
        f"Summary: {profile.get('summary','')}"
    )

    text_parts.append(
        f"Current Title: {profile.get('current_title','')}"
    )

    text_parts.append(
        f"Current Company: {profile.get('current_company','')}"
    )

    text_parts.append(
        f"Industry: {profile.get('current_industry','')}"
    )

    text_parts.append(
        f"Years Experience: {profile.get('years_of_experience','')}"
    )

    # Career History

    for job in candidate.get(
        "career_history",
        []
    ):

        text_parts.append(
            f"""
            Company: {job.get('company','')}
            Title: {job.get('title','')}
            Industry: {job.get('industry','')}
            Description: {job.get('description','')}
            Duration: {job.get('duration_months','')} months
            """
        )

    # Skills

    skill_text = []

    for skill in candidate.get(
        "skills",
        []
    ):

        skill_text.append(
            skill.get(
                "name",
                ""
            )
        )

    text_parts.append(
        "Skills: "
        + ", ".join(skill_text)
    )

    # Certifications

    certs = []

    for cert in candidate.get(
        "certifications",
        []
    ):

        certs.append(
            cert.get(
                "name",
                ""
            )
        )

    text_parts.append(
        "Certifications: "
        + ", ".join(certs)
    )

    # Languages

    langs = []

    for lang in candidate.get(
        "languages",
        []
    ):

        langs.append(
            lang.get(
                "name",
                ""
            )
        )

    text_parts.append(
        "Languages: "
        + ", ".join(langs)
    )

    # Education

    for edu in candidate.get(
        "education",
        []
    ):

        text_parts.append(
            f"""
            Education:
            Degree: {edu.get('degree','')}
            Field: {edu.get('field_of_study','')}
            """
        )

    return "\n".join(
        text_parts
    )
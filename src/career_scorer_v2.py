ROLE_BONUS = {

    # Core AI / ML Roles

    "machine learning": 10,
    "ml engineer": 15,
    "ai engineer": 15,

    "data scientist": 10,

    "mlops": 10,

    "nlp": 15,

    "applied scientist": 15,

    # Strong JD-aligned roles

    "recommendation systems engineer": 20,

    "search engineer": 20,

    "senior machine learning engineer": 20,

    "senior ai engineer": 20,

    "lead ai engineer": 20,

    "senior nlp engineer": 20,

    "applied ml engineer": 20,

    # Product ownership

    "tech lead": 10,

    "staff engineer": 10,

    "principal engineer": 0
}


CONSULTING_COMPANIES = [

    "tcs",
    "infosys",
    "wipro",
    "cognizant",
    "capgemini",
    "accenture",
    "genpact"
]


PRODUCT_COMPANIES = [

    "google",
    "meta",
    "amazon",
    "apple",
    "microsoft",
    "linkedin",

    "flipkart",
    "swiggy",
    "zomato",
    "cred",
    "razorpay",
    "ola",

    "zoho",
    "freshworks",
    "sarvam ai",
    "haptik",
    "policybazaar"
]


NEGATIVE_ROLES = [

    "marketing",
    "sales",
    "customer support",

    "accountant",
    "hr manager",

    "graphic designer",

    "civil engineer",
    "mechanical engineer"
]


VERY_NEGATIVE_ROLES = [

    "marketing manager",

    "hr manager",

    "accountant",

    "graphic designer",

    "customer support"
]


def career_score(candidate):

    score = 0

    profile = candidate.get(
        "profile",
        {}
    )

    years = profile.get(
        "years_of_experience",
        0
    )

    # JD prefers 5-9 years

    if years < 4:

        score -= 120

    elif years < 5:

        score -= 120

    elif 6 <= years <= 8:

        score += 40

    elif 5 <= years <= 10:

        score += 25

    elif 10 < years <= 12:

        score += 5

    elif years > 15:

        score -= 20

    elif years > 12:

        score -= 10

    found_keywords = set()

    found_companies = set()

    found_negative_roles = set()

    found_very_negative_roles = set()

    service_company_count = 0

    total_company_count = 0

    for job in candidate.get(
        "career_history",
        []
    ):

        title = job.get(
            "title",
            ""
        ).lower()

        description = job.get(
            "description",
            ""
        ).lower()

        combined = (
            title
            + " "
            + description
        )

        # Positive role signals

        for keyword, value in (
            ROLE_BONUS.items()
        ):

            if (
                keyword in combined
                and keyword not in found_keywords
            ):

                score += value

                found_keywords.add(
                    keyword
                )

        # Negative roles

        for role in NEGATIVE_ROLES:

            if (
                role in combined
                and role not in found_negative_roles
            ):

                score -= 20

                found_negative_roles.add(
                    role
                )

        # Very negative roles

        for role in VERY_NEGATIVE_ROLES:

            if (
                role in combined
                and role not in found_very_negative_roles
            ):

                score -= 40

                found_very_negative_roles.add(
                    role
                )

        company = job.get(
            "company",
            ""
        ).lower()

        total_company_count += 1

        if company in CONSULTING_COMPANIES:

            service_company_count += 1

            score -= 10

        if (
            company in PRODUCT_COMPANIES
            and company not in found_companies
        ):

            score += 5

            found_companies.add(
                company
            )

    # Entire career in consulting

    if (
        total_company_count > 0
        and service_company_count == total_company_count
    ):

        score -= 25

    score = min(score, 100)

    score = max(score, -100)

    return score
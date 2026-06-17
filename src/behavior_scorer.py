from datetime import datetime


def days_since(date_str):

    try:

        d = datetime.fromisoformat(
            date_str
        )

        return (
            datetime.now() - d
        ).days

    except Exception:

        return 9999


def behavior_score(
    signals,
    candidate_text=""
):

    score = 0

    # Open to work

    if signals.get(
        "open_to_work_flag"
    ):

        score += 20

    else:

        score -= 10

    # Recent activity

    last_active = days_since(

        signals.get(
            "last_active_date",
            "1900-01-01"
        )

    )

    if last_active <= 30:

        score += 15

    elif last_active <= 90:

        score += 8

    else:

        score -= 15

    # Recruiter response rate

    rr = signals.get(
        "recruiter_response_rate",
        0
    )

    if rr >= 0.5:

        score += 12

    elif rr >= 0.3:

        score += 8

    elif rr >= 0.1:

        score += 2

    else:

        score -= 10

    # Interview completion rate

    icr = signals.get(
        "interview_completion_rate",
        0
    )

    if icr >= 0.8:

        score += 10

    elif icr >= 0.6:

        score += 6

    elif icr >= 0.4:

        score += 2

    else:

        score -= 8

    # Verification

    if signals.get(
        "verified_email"
    ):

        score += 3

    if signals.get(
        "verified_phone"
    ):

        score += 3

    if signals.get(
        "linkedin_connected"
    ):

        score += 2

    # GitHub activity
    # Dataset uses approximately 0-10 scale

    gh = signals.get(
        "github_activity_score",
        0
    )

    if gh >= 8:

        score += 10

    elif gh >= 6:

        score += 7

    elif gh >= 4:

        score += 4

    elif gh >= 2:

        score += 2

    # Notice period

    notice = signals.get(
        "notice_period_days",
        180
    )

    if notice <= 30:

        score += 6

    elif notice <= 60:

        score += 3

    elif notice >= 120:

        score -= 5

    # Recruiter interest

    saved = signals.get(
        "saved_by_recruiters_30d",
        0
    )

    if saved >= 10:

        score += 10

    elif saved >= 5:

        score += 5

    elif saved >= 1:

        score += 2

    # Profile completeness

    completeness = signals.get(
        "profile_completeness_score",
        0
    )

    if completeness >= 90:

        score += 5

    elif completeness >= 75:

        score += 3

    elif completeness >= 50:

        score += 1

    return min(
        score,
        100
    )
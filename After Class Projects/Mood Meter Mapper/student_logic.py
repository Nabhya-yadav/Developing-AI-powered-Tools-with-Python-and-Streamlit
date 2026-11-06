from constants import DEFAULT_SCORE, MAX_SCORE, MIN_SCORE, MOOD_RULES


def clamp_score(score: int) -> int:
    """Keep the score safely inside the 0-100 range."""
    return max(MIN_SCORE, min(MAX_SCORE, int(score)))



def get_mood_label(score: int) -> str:
    """Convert a trust score into its matching mood label."""
    score = clamp_score(score)

    if score < 20:
        return "Suspicious"
    elif score < 50:
        return "Watching"
    elif score < 80:
        return "Curious"
    return "Accepting"



def get_mood_data(score: int) -> dict:
    """Return the full mood dictionary used by the UI."""
    score = clamp_score(score)
    label = get_mood_label(score)

    for mood in MOOD_RULES:
        if mood["label"] == label:
            return mood

    return MOOD_RULES[1]



def get_progress_message(score: int) -> str:
    """Give a short progress note for the current trust score."""
    score = clamp_score(score)

    if score < 20:
        return "Start with stronger positive actions to raise trust."
    elif score < 50:
        return "The score is moving up. Keep building trust carefully."
    elif score < 80:
        return "Great progress. The system is nearly fully convinced."
    return "Excellent. Trust is strong and the system has accepted the score."



def default_state() -> dict:
    return {"score": DEFAULT_SCORE}
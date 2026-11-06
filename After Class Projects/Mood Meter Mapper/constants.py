APP_TITLE = "Mood Meter Mapper"
APP_ICON = "🎭"

MIN_SCORE = 0
MAX_SCORE = 100
DEFAULT_SCORE = 45

SCENARIO_PRESETS = {
    "Broken Trust": 10,
    "Careful Progress": 35,
    "Almost There": 68,
    "Gate Open": 90,
}

MOOD_RULES = [
    {
        "label": "Suspicious",
        "min": 0,
        "max": 19,
        "color": "#ef4444",
        "emoji": "🛑",
        "summary": "The system does not trust the score yet.",
    },
    {
        "label": "Watching",
        "min": 20,
        "max": 49,
        "color": "#f59e0b",
        "emoji": "👀",
        "summary": "Trust is improving, but the system is still cautious.",
    },
    {
        "label": "Curious",
        "min": 50,
        "max": 79,
        "color": "#06b6d4",
        "emoji": "✨",
        "summary": "The score looks promising and the system is opening up.",
    },
    {
        "label": "Accepting",
        "min": 80,
        "max": 100,
        "color": "#22c55e",
        "emoji": "✅",
        "summary": "Trust is high and the system fully accepts the score.",
    },
]
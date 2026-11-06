REQUIRED_KEYS = ["title", "description", "clue", "art_prompt"]

ROOM_FALLBACK = {
    "description": (
        "{room_name} opens in eerie silence. The {theme} glows softly through the dark, "
        "and the air feels {mood}, as if the chamber is waiting to be understood."
    ),
    "clue": "A faint shimmer near the wall suggests that the room is hiding a secret.",
    "art_prompt": (
        "A fantasy chamber called {room_name}, themed around {theme}, "
        "with a {mood} atmosphere, cinematic lighting, ultra detailed environment art"
    ),
}
import streamlit as st
from constants import MAX_SCORE, MIN_SCORE, MOOD_RULES, SCENARIO_PRESETS


def render_header() -> None:
    st.title("🎭 Mood Meter Mapper")
    st.caption("Convert a trust score into a live mood label using threshold mapping.")



def render_score_input(current_score: int) -> int:
    return st.slider(
        "Choose the trust score",
        min_value=MIN_SCORE,
        max_value=MAX_SCORE,
        value=current_score,
        help="Move the slider to see how the mood changes across thresholds.",
    )



def render_quick_actions() -> str | None:
    st.markdown("### Quick scenarios")
    columns = st.columns(len(SCENARIO_PRESETS))
    selected_label = None

    for column, (label, value) in zip(columns, SCENARIO_PRESETS.items()):
        if column.button(f"{label} ({value})", use_container_width=True):
            selected_label = label

    return selected_label



def render_mood_card(score: int, mood: dict, message: str) -> None:
    st.markdown(
        f"""
        <div style="border:1px solid #e5e7eb; border-left:8px solid {mood['color']};
                    border-radius:16px; padding:18px; margin-top:14px; background:#ffffff;">
            <div style="font-size:32px;">{mood['emoji']}</div>
            <div style="font-size:26px; font-weight:700; color:#111827; margin-top:6px;">{mood['label']}</div>
            <div style="font-size:15px; color:#4b5563; margin-top:6px;">Trust score: <strong>{score}</strong></div>
            <div style="font-size:15px; color:#374151; margin-top:8px;">{mood['summary']}</div>
            <div style="font-size:14px; color:#6b7280; margin-top:10px;">{message}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )



def render_rules_table() -> None:
    st.markdown("### Mapping rules")
    rows = [
        {
            "Mood": mood["label"],
            "Range": f"{mood['min']} - {mood['max']}",
            "Meaning": mood["summary"],
        }
        for mood in MOOD_RULES
    ]
    st.table(rows)



def render_reset() -> bool:
    return st.button("Reset to default score", use_container_width=True)
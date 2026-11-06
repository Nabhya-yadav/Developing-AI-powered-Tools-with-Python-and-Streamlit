import streamlit as st
from constants import APP_ICON, APP_TITLE


def setup_page() -> None:
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=APP_ICON,
        layout="centered",
        initial_sidebar_state="collapsed",
    )
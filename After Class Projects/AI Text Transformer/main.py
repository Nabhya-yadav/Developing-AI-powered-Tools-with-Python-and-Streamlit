import streamlit as st

from ui import inject_css, render_header, render_output, render_empty_state
from student_logic import transform_text
from constants import STYLE_OPTIONS

st.set_page_config(
    page_title="AI Text Transformer",
    page_icon="✨",
    layout="centered",
)

inject_css()
render_header()

if "output_text" not in st.session_state:
    st.session_state.output_text = ""

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "selected_style" not in st.session_state:
    st.session_state.selected_style = STYLE_OPTIONS[0]

st.markdown("### Enter your original text")

input_text = st.text_area(
    label="Enter your original text",
    value=st.session_state.input_text,
    placeholder="Paste your plain text here...",
    height=220,
    label_visibility="collapsed",
)

col1, col2 = st.columns(2)

with col1:
    selected_style = st.selectbox(
        "Choose a rewrite style",
        STYLE_OPTIONS,
        index=STYLE_OPTIONS.index(st.session_state.selected_style)
        if st.session_state.selected_style in STYLE_OPTIONS else 0,
    )

with col2:
    st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
    transform_clicked = st.button("Transform Text", use_container_width=True)

st.session_state.input_text = input_text
st.session_state.selected_style = selected_style

if transform_clicked:
    if input_text.strip():
        st.session_state.output_text = transform_text(input_text, selected_style)
    else:
        st.session_state.output_text = ""

st.markdown("### Output")

output_text = st.session_state.output_text

if output_text:
    render_output(output_text)
else:
    render_empty_state()

st.caption("The meaning stays the same. Only the style changes.")
import base64
from io import BytesIO

import streamlit as st
from PIL import Image
from groq import Groq
from config import (
    APP_TITLE,
    APP_SUBTITLE,
    GROQ_API_KEY,
    MODEL_NAME,
    STYLES,
    build_prompt,
)

st.set_page_config(page_title=APP_TITLE, page_icon="🍽️", layout="centered")

def encode_image_to_base64(image: Image.Image) -> str:
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

def review_food_image(image: Image.Image, style_key: str) -> str:
    client = Groq(api_key=GROQ_API_KEY)
    prompt = build_prompt(style_key)
    image_base64 = encode_image_to_base64(image)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{image_base64}"},
                    },
                ],
            }
        ],
        temperature=0.7,
        max_tokens=450,
    )
    return response.choices[0].message.content

st.title(APP_TITLE)
st.caption(APP_SUBTITLE)

with st.container(border=True):
    st.subheader("Upload and review")
    uploaded_file = st.file_uploader(
        "Upload a food image",
        type=["png", "jpg", "jpeg", "webp"],
    )
    style_key = st.selectbox("Choose review style", list(STYLES.keys()))

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded food image", use_container_width=True)

    with st.expander("See review style instruction"):
        st.code(STYLES[style_key], language="text")

    if not GROQ_API_KEY or GROQ_API_KEY == "your_groq_api_key_here":
        st.warning("Add your Groq API key in the .env file before generating the review.")

    if st.button("Review food image", use_container_width=True, type="primary"):
        if not GROQ_API_KEY or GROQ_API_KEY == "your_groq_api_key_here":
            st.error("Groq API key is missing. Update the .env file and try again.")
        else:
            with st.spinner("Analyzing the food image and writing the review..."):
                try:
                    review = review_food_image(image, style_key)
                    st.success("Review generated successfully.")
                    st.subheader("AI Food Review")
                    st.markdown(review)
                except Exception as error:
                    st.error(f"Could not generate the review right now. {error}")

st.markdown("---")
st.markdown(
    "**What this project teaches:** Vision Language Models, STYLES dictionary, "
    "Python functions, file uploads, base64 encoding, Groq Chat Completions API, "
    "and controlling AI output with prompt instructions."
)
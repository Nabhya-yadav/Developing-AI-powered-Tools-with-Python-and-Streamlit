from groq import Groq
import config
from constants import STYLE_PROMPTS


def local_transform(text:str, style:str) -> str:
    simple_rewrites = {
        "Professional": f"Here is a more professional version: {text}",
        "Friendly": f"Here is a warmer, friendlier version:{text}",
        "Concise": f"Here is a shorter, clearer version:{text}",
        "Storytelling": f"Here is a more engaging storytelling version:{text}",
        "Formal": f"Here is a more formal version:{text}",
        "Persuasive": f"Here is a more persuasive version:{text}",
    }
    return simple_rewrites.get(style, text).strip() 


def transform_text(text: str, style: str) -> str:
    text = text.strip()

    if not text:
        return ""

    if not config.GROQ_API_KEY:
        return local_transform(text, style)

    style_instruction = STYLE_PROMPTS.get(
        style,
        "Rewrite the text in a better style while keeping the meaning unchanged."
    )

    system_prompt = (
        "You are an expert text transformation assistant. "
        "Your task is to rewrite text in a requested style while preserving the original meaning. "
        "Do not add new facts. Do not remove key meaning. Keep the rewritten output natural and polished."
    )

    user_prompt = (
        f"{style_instruction}"
        f"Original text:{text}"
        "Return only the rewritten text."
    )

    try:
        client = Groq(api_key=config.GROQ_API_KEY)
        response = client.chat.completions.create(
            model=config.GROQ_TEXT_MODEL,
            temperature=0.8,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return local_transform(text, style)
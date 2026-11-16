import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.models.get("gemini-3.8-flash")

def load_prompt():
    with open("Prompts/prompt.txt", "r") as f:
        return f.read()

PROMPT_TEMPLATE = load_prompt()
def ask_gemini(question, context):
    prompt = PROMPT_TEMPLATE.format(context=context, question=question)
    response = gemini_model.generate_text(prompt)
    return response.text
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
resp = client.models.generate_content(
    model="gemma-4-26b-a4b-it",
    contents="Say something about Purdue in one line."
)
print(resp.text)
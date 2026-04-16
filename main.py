import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
model = "gemini-2.5-pro"

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model=model,
    contents="Explain how AI works in a few words",
)

print(response.text)
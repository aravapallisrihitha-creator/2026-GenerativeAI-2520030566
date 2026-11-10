from dotenv import load_dotenv
from google import genai
import os
from pathlib import Path

# Step 1: Load API key
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# Step 2: Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Step 3: Initialize Gemini client
client = genai.Client(api_key=api_key)

# Step 4: Make first LLM call
try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="What is Machine Learning? Explain in simple words."
    )

    # Step 5: Display response
    print("\nLLM Response:")
    print(response.text)

except Exception as e:
    print("\nSomething went wrong:")
    print(e)
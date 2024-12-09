import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

while True:
    prompt = input("prompt (ketik 'quit' untuk keluar): ")
    if prompt.lower() == 'quit':
        print("Keluar dari program")
        break
    try:
        response = model.generate_content(prompt)
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")
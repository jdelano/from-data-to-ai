from openai import OpenAI
import dotenv
import os
dotenv.load_dotenv()  # Load variables from .env file
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
history = [{"role":"system","content":"You are ..."}]
while True:
    user = input("You: ")
    history.append({"role":"user","content":user})
    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=history
    )
    answer = resp.choices[0].message.content
    print("Bot:", answer)
    history.append({"role":"assistant","content":answer})
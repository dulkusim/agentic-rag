import os
from dotenv import load_dotenv
from ollama import Client

load_dotenv()

client = Client(host = os.getenv("OLLAMA_HOST"))

SYSTEM_PROMPT = """You are a financial advisor.
                Don't answer questions that are not related to finances."""

messages = [{"role": "system", "content": SYSTEM_PROMPT}]

while True:

    user_input = input("User: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat(
        model = "qwen3.6:latest",
        messages = messages
    )

    assistant_message = response["message"]["content"] 
    messages.append({"role": "assistant", "content": assistant_message})
    print("Assistant: ", assistant_message)
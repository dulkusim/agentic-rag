#LLM Wrapper
from ollama import Client
import config

client = Client(host = config.OLLAMA_HOST)

def generate(messages):
    return client.chat(
        model = config.MODEL,
        messages = messages,
        )
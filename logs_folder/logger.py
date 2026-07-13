# logs/logger.py
from datetime import datetime

LOG_FILE = "logs_folder/logs.txt"

def log_timestamp():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def start_conversation(system_prompt, context):

    with open(LOG_FILE, "w", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write(f"Conversation started: {log_timestamp()}\n")
        file.write("=" * 60 + "\n\n")

        file.write("SYSTEM PROMPT\n")
        file.write(system_prompt + "\n\n")

        file.write("ASSISTANT MESSAGE\n")
        file.write(context + "\n\n")


def log_turn(user_input, assistant_response):

    with open(LOG_FILE, "a", encoding="utf-8") as file:

        file.write(f"[{log_timestamp()}]\n")

        file.write(f"User: {user_input}\n")

        file.write(f"Assistant: {assistant_response}\n")

        file.write("-" * 60 + "\n")
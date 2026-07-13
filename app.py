from llm import llm_wrapper
from logs_folder.logger import start_conversation, log_turn

with open("./prompts/restaurant_system.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

with open("./prompts/restaurant_context.txt", "r", encoding="utf-8") as f:
    ASSISTANT_MESSAGE = f.read()

messages = [{"role": "system", "content": SYSTEM_PROMPT},
            {"role": "assistant", "content": ASSISTANT_MESSAGE}]

start_conversation(SYSTEM_PROMPT, ASSISTANT_MESSAGE)

while True:
    user_input = input("User: ")
    
    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": user_input})

    response = llm_wrapper.generate(messages=messages)

    assistant_message = response["message"]["content"]
    print(assistant_message)
    messages.append({"role": "assistant", "content": assistant_message})
    
    log_turn(user_input, assistant_message)
"""
Day 6 - Save Conversations - Persist to JSON file
Use Python's `json` module to save `conversation_history` to a file when user quits, and load it on startup.
"""


# Import statements
import json
import anthropic
import httpx 
from dotenv import load_dotenv

load_dotenv()

http_client = httpx.Client(verify=False)

client = anthropic.Anthropic(http_client=http_client)

def call_claude(user_message, conversation_history):
    conversation_history.append({"role": "user", "content": user_message})

    with client.messages.stream(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system="You are a helpful assistant. Be courtious, but skeptical and scientifically rigorous.",
        messages=conversation_history
    ) as stream:
        print()
        for text in stream.text_stream:
            print(text, end="", flush=True)

    final_message = stream.get_final_message()
    assistant_response = final_message.content[0].text 

    print()

    conversation_history.append({'role': 'assistant', 'content': assistant_response})
    with open('conversation.json', 'w') as f:
        json.dump(conversation_history, f, indent=2)

    print(f"\nConversation history:\n{conversation_history}\n")


if __name__ == "__main__":
    try: 
        with open('conversation.json', 'r') as f:
            print("\nReading from conversation history file...\n")
            conversation_history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nCreating conversation history file...\n")
        conversation_history = []
        with open('conversation.json', 'w') as f:
            json.dump(conversation_history, f, indent=2)

    while True:
        user_question = input("\nUser: ")
        if user_question.lower() == "quit":
            break
        call_claude(user_question, conversation_history)
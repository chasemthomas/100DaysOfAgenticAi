"""
 Day 7 - Error Handling - Network errors, rate limits, graceful failures
Wrap API calls in try/except blocks to catch `APIError`, `APIConnectionError`, and `RateLimitError`. Display friendly error messages.
"""
import json
import anthropic 
from anthropic import APIError, APIConnectionError, RateLimitError
import httpx
from dotenv import load_dotenv

load_dotenv()
http_client = httpx.Client(verify=False)
client = anthropic.Anthropic(http_client=http_client)

CONVERSATION_HISTORY = "Challenges/conversation.json"
SYSTEM_MESSAGE = "You are a helpful assistant. be courtious, but skeptical and scientifically rigorous."

# Load history 
def load_history():
    try:
        with open(CONVERSATION_HISTORY, 'r') as f:
            print("\nReading from conversation history file...\n")
            return json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        print("\nCreating conversation history file...\n")
        with open(CONVERSATION_HISTORY, 'w') as f:
            return json.load("", f, indent=2)

def save_history(history):
    with open(CONVERSATION_HISTORY, 'w') as f:
        json.dump(history, f, indent=2)
    
# Update history
def append_history(role, content, history):
    return history.append({"role": role, "content" : content})

# Streamer 
def start_streamer(conversation_history, user_message):
    try:
        with client.messages.stream(
            model="claude-haiku-4-5",
            max_tokens=1024,
            system=SYSTEM_MESSAGE,
            messages=conversation_history
        ) as stream:
            print()
            for text in stream.text_stream:
                print(text, end="", flush=True)

        assistant_message = stream.get_final_message()
        assistant_response = assistant_message.content[0].text
        append_history("user", user_message, conversation_history)
        append_history("assistant", assistant_response, conversation_history)
        save_history(conversation_history)
        return 
    except RateLimitError:
        print("Rate limit reached. Please wait and try again.")
        return
    except APIConnectionError:
        print("Network error. Please check your connection.")
        return
    except APIError:
        print("The API returned an error. Please try again later.")
        return
    except KeyboardInterrupt:
        print("\nStream interrupted by user.")
        return


def call_claude(user_message, conversation_history):
    start_streamer(conversation_history, user_message)
    return


if __name__ == "__main__":
    conversation_history = load_history()

    while True:
        user_question = input("User: ")
        if user_question.lower() == "quit":
            break
        call_claude(user_question, conversation_history)
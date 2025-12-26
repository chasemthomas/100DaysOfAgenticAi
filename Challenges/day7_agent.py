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
SYSTEM_MESSAGE = "You are a helpful assistant. be courteous, but skeptical and scientifically rigorous."

# Load history 
def load_history(CONVERSATION_HISTORY):
    try:
        with open(CONVERSATION_HISTORY, 'r') as f:
            print("\nReading from conversation history file...\n")
            return json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        print("\nCreating conversation history file...\n")
        with open(CONVERSATION_HISTORY, 'w') as f:
            return []

def save_history(history):
    try:    
        with open(CONVERSATION_HISTORY, 'w') as f:
            json.dump(history, f, indent=2)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nCould not save conversation history file.\n")
        return
    except Exception:
        print("\nCould not save conversation history file.\n")
        return
    
# Update history
def append_history(role, content, history):
    try:
        history.append({"role": role, "content" : content})
    except Exception:
        print("\nCould not append conversation history. Invalid role or content.\n")
        return
    return

def save_history(history):
    try:
        with open(CONVERSATION_HISTORY, 'w') as f:
            json.dump(history, f, indent=2)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nCould not save conversation history file.\n")
        return
    except Exception:
        print("\nCould not save conversation history file.\n")
        return

# Streamer 
def start_streamer(conversation_history, user_message):
    append_history("user", user_message, conversation_history)
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
        append_history("assistant", assistant_response, conversation_history)
        save_history(conversation_history)
        return 
    except RateLimitError:
        print("Rate limit reached. Please wait and try again.")
        append_history("assistant", "Rate limit reached. Please wait and try again.", conversation_history)
        save_history(conversation_history)
        return
    except APIConnectionError:
        print("Network error. Please check your connection.")
        append_history("assistant", "Network error. Please check your connection.", conversation_history)
        save_history(conversation_history)
        return
    except APIError:
        print("The API returned an error. Please try again later.")
        append_history("assistant", "The API returned an error. Please try again later.", conversation_history)
        save_history(conversation_history)
        return
    except KeyboardInterrupt:
        print("\nStream interrupted by user.")
        append_history("assistant", "Stream interrupted by user.", conversation_history)
        save_history(conversation_history)
        return

if __name__ == "__main__":
    conversation_history = load_history(CONVERSATION_HISTORY)

    while True:
        user_question = input("\nUser: ")
        if user_question.lower() == "quit":
            break
        start_streamer(conversation_history, user_question)
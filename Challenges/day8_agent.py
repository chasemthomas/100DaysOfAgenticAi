"""
Day 8: First Tool - get_current_time() function
Create a simple Python function that returns current time. Define it in the `tools` parameter and let Claude decide when to call it.
  """
from cgitb import text
import json
from anthropic import Anthropic, APIError, APIConnectionError, RateLimitError
import httpx
from dotenv import load_dotenv
import argparse
from datetime import datetime
import os

load_dotenv()
http_client = httpx.Client(verify=False)
client = Anthropic(http_client=http_client)

SYSTEM_MESSAGE = "You are a helpful assistant. Be courteous, but skeptical and scientifically rigorous."

def load_history(json_file_path=None): 
  """
    Load conversation history from a JSON file.
    
    Args:
        json_file_path (str, optional): Path to the JSON file to load. 
                                       If None, creates a new timestamped file.
    
    Returns:
        tuple: (conversation_history_list, file_path_used)
    """

  # If not file path provided, create a timestamped filename
  if json_file_path is None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_file_path = f"conversations/conversation_{timestamp}.json"
    print(f"\nNo conversation file specified. Creating new file: {json_file_path}")

  # Ensure the directory exists
  os.makedirs(os.path.dirname(json_file_path), exist_ok=True)

  try:
    with open(json_file_path, 'r') as f:
      print(f"\nReading from conversation history file {json_file_path}")
      history = json.load(f)
      return history, json_file_path

  except FileNotFoundError:
    print(f"\nFile not found. Creating conversation history file {json_file_path}")
    with open(json_file_path, 'w') as f:
      json.dump([], f)
      return [], json_file_path
    
  except  json.JSONDecodeError:
    print(f"\nInvalid JSON in File: {json_file_path}. Creating new file.\n")
    with open(json_file_path, 'w') as f:
      json.dump([], f)
    return [], json_file_path

def save_history(history, file_path):
  try:
    with open(file_path, 'w') as f:
      json.dump(history, f, indent=2)
  
  except (FileNotFoundError, json.JSONDecodeError):
    print("\nCould not save conversation history file.\n")
    return 

def append_history(role, content, history, file_path):
  try:
    history.append({'role': role, 'content': content})
  
  except Exception as e:
    print("\nCould not append confersation history: {e}\n")
    return 
  return 


def start_streamer(conversation_history, file_path, user_message):
  append_history("user", user_message, conversation_history, file_path)

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
    append_history("assistant", assistant_response, conversation_history, file_path)
    save_history(conversation_history, file_path)
    print()
  
  except RateLimitError as e: 
    print("\nRate limit reached. Please wait and try again. Exception: {e}\n")
    append_history("assistant", "Rate limit reached. Please wait and try again.", conversation_history, file_path)
    save_history(conversation_history, file_path)
    return
  
  except APIConnectionError as e:
    print("Nework Error. Please check your connection. Exception: {e}\n")
    append_history("assistant", "Network error. Please check your connection.", conversation_history, file_path)
    save_history(conversation_history, file_path)
    return

  except APIError as e:
    print("The API returned an error. Please try again later.Exception: {e}\n")
    append_history("assistant", "The API returned an error. Please try again later.", conversation_history, file_path)
    save_history(conversation_history, file_path)
    return

  except KeyboardInterrupt as e:
    print("\nStream interrupted by user. Exception: {e}\n")
    append_history("assistant", "Stream interrupted by user.", conversation_history, file_path)
    save_history(conversation_history, file_path)
    return

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 8 Agent with conversation history")
  parser.add_argument('--history', type=str, default=None, 
                      help='Path to JSON file containing conversation history')
  
  args = parser.parse_args()

  conversation_history, history_file = load_history(args.history)

  print(f"\nLoaded conversation history from: {history_file}")
  print(f"\nHistory contains {len(conversation_history)} messages")

  while True:
    user_question = input("\nUser: ")
    if user_question.lower() in ["quit", "exit"]:
      break
    start_streamer(conversation_history, history_file, user_question)



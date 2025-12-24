"""
Day 2: User Input Loop - Accept ongoing conversation

Wrap your API call in a while True loop that takes user input and displays responses until user types 'quit'.
"""

import os
import anthropic
import httpx
from dotenv import load_dotenv
load_dotenv()

http_client = httpx.Client(verify=False)
client = anthropic.Anthropic(http_client=http_client)

def call_claude(user_message):
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": user_message}]
    )
    return message.content[0].text

if __name__ == "__main__":
    while True:
        user_question = input("User: ")
        if user_question.lower() == "quit" or user_question.lower() == exit:
            break
        else:
            print(call_claude(user_question))   


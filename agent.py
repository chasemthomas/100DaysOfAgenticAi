"""
My AI Agent - 100 Day Build

Day 1: Get your first API response
Goal: Send a message to Claude/OpenAI and print the response

Start here!
"""

# Your code begins here
import os
import anthropic
import httpx
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

# Disable SSL verification (workaround for corporate proxy/firewall)
http_client = httpx.Client(verify=False)
client = anthropic.Anthropic(api_key=api_key, http_client=http_client)

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content":"Hello Claude!"
        }
    ]
)

print(message.content)
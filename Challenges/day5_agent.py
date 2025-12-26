'''
Day 5 - System Prompts - Add agent personality
Add a [system](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/system-prompts) parameter to your API call with instructions that define your agent's personality, tone, and expertise.
'''

import anthropic 
import httpx
from dotenv import load_dotenv

load_dotenv()

http_client = httpx.Client(verify=False)

client = anthropic.Anthropic(http_client=http_client)

system_message = "You are a helpful assistant. Be courtious, but skeptical and scientifically rigorous."

def call_claude(user_message, conversation_history=None):
    if conversation_history is None:
        conversation_history = []

    conversation_history.append({"role": "user", "content": user_message})

    with client.messages.stream(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system=system_message,
        messages=conversation_history
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
    
    final_message = stream.get_final_message()
    assistant_response = final_message.content[0].text

    print()

    conversation_history.append({'role': 'assistant', 'content': assistant_response})

    print(f"\nConversation History\n{conversation_history}\n")

if __name__ == "__main__":
    conversation_history = []

    while True:
        user_question = input(f"\nUser:")
        if user_question.lower() == "quit":
            break
        print('\n')
        call_claude(user_question, conversation_history)
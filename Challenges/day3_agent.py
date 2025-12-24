'''
Day 3 - Conversation Memory - Track message history
Create a `conversation_history` list that stores all user and assistant messages. Pass this full history to each API call.
'''

import anthropic
from dotenv import load_dotenv
import httpx

load_dotenv()

http_client = httpx.Client(verify=False)
client = anthropic.Anthropic(http_client=http_client)

def call_claude(user_message, conversation_history=None):

    if conversation_history is None:
        conversation_history = []

    conversation_history.append({"role": "user", "content" : user_message})

    message = client.messages.create(
        model="claude-sonnet-4-5" ,
        max_tokens=1024, 
        messages=conversation_history,
    )

    assistant_response = message.content[0].text
    conversation_history.append({"role":"assistant", "content": assistant_response})

    print(assistant_response)
    print(f'\nConversation History\n{conversation_history}\n')
    return assistant_response
    

if __name__ == "__main__": 
    conversation_history = []

    while True:
        user_question = input("\nUser: ")
        if user_question.lower() == "quit":
            break
        print('\n')
        call_claude(user_question, conversation_history)
'''
Day 4 - Streaming Responses - Real-time token display
Change it to display words as they're generated instead of waiting for complete response.
See documentation on [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming)
'''
import anthropic
import httpx 
from dotenv import load_dotenv

load_dotenv()

http_client = httpx.Client(verify=False)

client = anthropic.Anthropic(http_client=http_client)

def call_claude(user_message, conversation_history=None):
    if conversation_history is None:
        conversation_history = []
    
    conversation_history.append({"role": "user", "content": user_message})

    with client.messages.stream(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=conversation_history
    ) as stream:
        for text in stream.text_stream:
            print(text,end="", flush=True)


    final_message = stream.get_final_message()
    assistant_response = final_message.content[0].text

    print()
    
    conversation_history.append({"role": "assistant", "content": assistant_response})
    
    print(f"\nConversation History\n{conversation_history}\n")

    return assistant_response


if __name__ == "__main__": 
    conversation_history = []

    while True:
        user_question = input(f"\nUser: ")
        if user_question.lower() == "quit":
            break 
        print('\n')
        call_claude(user_question, conversation_history)
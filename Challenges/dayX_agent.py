'''
Day 3 - Conversation Memory - Track message history
Create a `conversation_history` list that stores all user and assistant messages. Pass this full history to each API call.
'''

# Think about what libraries you need for API calls, environment variables, and HTTP requests
# TODO: Import statements here

# Load environment variables (you'll need this for API keys)
# TODO: Load dotenv

# Set up an HTTP client that doesn't verify SSL certificates
# TODO: Create httpx client with verify=False

# Create an Anthropic client instance using the HTTP client
# TODO: Initialize Anthropic client

# Define a function that takes a user message and optional conversation history
# What should the default value be if no history is provided?
def call_claude(user_message, conversation_history=None):
    # If no conversation history was passed, what should you initialize?
    # TODO: Handle None case
    
    # Before making the API call, you need to add the user's message to the history
    # What format does the Anthropic API expect? (hint: it's a dictionary with "role" and "content")
    # TODO: Append user message to conversation_history
    
    # Make the API call to Claude
    # What model did you use before? (hint: it's a sonnet model, version 4-5)
    # What parameter should you use to pass the conversation history? (hint: it's not in the prompt!)
    # Set max_tokens to 1024
    # TODO: Call client.messages.create()
    
    # Extract the assistant's response from the message object
    # How did you access the text content before? (hint: message.content[0].text)
    # TODO: Get assistant_response
    
    # Don't forget to add the assistant's response to the conversation history!
    # What role should it have?
    # TODO: Append assistant response to conversation_history
    
    # Print the assistant's response
    # TODO: Print statement
    
    # Print the full conversation history for debugging
    # TODO: Print conversation_history
    
    # Return the assistant's response
    # TODO: Return statement
    pass


if __name__ == "__main__": 
    # Initialize an empty list to store the conversation history
    # TODO: Create conversation_history list
    
    # Create a loop that runs until the user wants to quit
    # How do you get user input? (hint: input() function)
    # What should the prompt say?
    # TODO: while True loop with input()
    
    # Check if the user wants to quit (case-insensitive check)
    # TODO: Break condition
    
    # Print a newline for spacing
    # TODO: Print newline
    
    # Call your function with the user's question and the conversation history
    # Why is it important to pass the conversation_history here?
    # TODO: Call call_claude()
    pass

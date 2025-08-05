import openai
import os
import dotenv

 # Load variables from .env file
dotenv.load_dotenv() 
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)

# Set the model name
model_name = "gpt-4o-mini"

# Introduce the chatbot to the user
print("Chatbot: Hello! I am a chatbot. Ask me anything.")
print("(Type 'stop' to end the conversation.)")

# Start the conversation loop
while True:
    # Get user input
    user_input = input("You: ")
    
    # Check for exit condition
    if user_input.lower() == "stop":
        print("Chatbot: Goodbye!")
        break
    
    # Generate a response using the Responses API
    response = openai.responses.create(
        model=model_name,
        input=user_input,
        instructions="You are a friendly and knowledgeable chatbot."
    )
    
    # Print the chatbot's response
    print(f"Chatbot: {response.output_text}")
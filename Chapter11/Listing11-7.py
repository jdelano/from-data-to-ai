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

# Open a log file in append mode
logfile = open("Chapter11/chat_log.txt", "a", encoding="utf-8")

# Introduce the chatbot to the user
print("Chatbot: Hello! I am a chatbot. Ask me anything.")
print("(Type 'stop' to end the conversation.)")

# Begin with no previous response
response = None

while True:
    user_input = input("You: ")
    
    # Check for exit condition
    if user_input.lower() == "stop":
        print("Chatbot: Goodbye!")
        break
    
    # Log the user's input
    logfile.write(f"User: {user_input}\n")
    
    if response is None:
        response = openai.responses.create(
            model=model_name,
            input=user_input,
            instructions="You are a friendly and knowledgeable chatbot."
        )
    else:
        response = openai.responses.create(
            model=model_name,
            input=user_input,
            previous_response_id=response.id
        )
    
    # Log the AI's response
    logfile.write(f"Assistant: {response.output_text}\n")
    logfile.flush()  # Ensure it writes to disk immediately
    
    print(f"Chatbot: {response.output_text}")
logfile.write("=== Conversation ended ===\n")
# Close the log file when done
logfile.close()
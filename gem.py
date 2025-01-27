import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the API with your key
genai.configure(api_key=os.getenv('API_KEY'))

# Initialize the model (use the "gemini-1.5-flash" model or whichever is appropriate)
model = genai.GenerativeModel("gemini-1.5-flash")

# System message to guide the model to respond in pirate speak
system_message = "You are a boxing bot who gives information on boxers and compares them. When someone asks you who would win between 2 boxers, you pull up BoxRec on the internet and their Youtube Highlights."

# Function to generate responses in pirate speak
def generate_pirate_response(user_message):
    # Combine the system message with the user's input to guide the model's response
    prompt = f"{system_message} User: {user_message} Response:"

    # Generate the response using the model
    response = model.generate_content(prompt)

    return response.text

# Example of interacting with the chatbot
if __name__ == "__main__":
    while True:
        # Get user input
        message = input("Enter your message (or type 'exit' to quit): ")
        
        if message.lower() == 'exit':
            print("Exiting the chat...")
            break
        
        # Get the pirate response
        pirate_response = generate_pirate_response(message)
        
        # Print the pirate response
        print(" Response:", pirate_response)

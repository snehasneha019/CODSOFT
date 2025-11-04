# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()  # make input case-insensitive

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! How about you?"
    
    elif "your name" in user_input:
        return "I'm a simple chatbot created to demonstrate rule-based responses."
    
    elif "weather" in user_input:
        return "I can’t check live weather, but I hope it’s nice where you are!"
    
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    
    else:
        return "I'm not sure I understand. Could you rephrase that?"

# Main conversation loop
print("Chatbot: Hello! I'm your rule-based chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    
    if "bye" in user_input.lower():
        break

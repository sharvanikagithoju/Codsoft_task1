import random

# Define rules and responses
rules = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm not sure how to respond to that.", "Could you please rephrase that?", "I didn't understand."],
}

# Define function to generate response based on input
def get_response(message):
    message = message.lower()
    for key in rules:
        if key in message:
            return random.choice(rules[key])
    return random.choice(rules["default"])

# Main loop to interact with the user
print("Chatbot: Hello! How can I help you?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
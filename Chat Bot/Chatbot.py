from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot("MyChatBot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language corpus data
trainer.train("chatterbot.corpus.english")

# Simple function to get a response from the chatbot
def get_response(user_input):
    return chatbot.get_response(user_input)

# Main loop for chatting
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Exiting...")
        break
    
    response = get_response(user_input)
    print(f"ChatBot: {response}")

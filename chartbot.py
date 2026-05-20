# Basic Rule-Based Chatbot

def chatbot():
    print("Simple Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks what about you !")

        elif user == "what is your name":
            print("Bot: I am a simple chatbot.")

        elif user == "tell me somthing":
            print("Bot: How was the day") 

        elif user == "it's okay not bad":
            print("Bot: ohh what happend i am here for you")      

        elif user == "bye":
            print("Bot: Goodbye Have a Good Day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()

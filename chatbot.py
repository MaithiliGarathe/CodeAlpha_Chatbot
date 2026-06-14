# Basic Chatbot - CodeAlpha Internship

def chatbot():
    print("=" * 40)
    print("   Welcome to CodeAlpha Chatbot! 🤖")
    print("=" * 40)
    print("Type 'bye' to exit\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "":
            print("Bot: Please say something!\n")

        elif user_input in ["hello", "hi", "hey"]:
            print("Bot: Hi! How are you? 😊\n")

        elif user_input in ["how are you", "how r you", "how are u"]:
            print("Bot: I'm fine, thanks! How about you? 😄\n")

        elif user_input in ["i am fine", "i'm fine", "good", "fine"]:
            print("Bot: Great to hear that! 😊\n")

        elif user_input in ["what is your name", "what's your name"]:
            print("Bot: I am CodeAlpha Chatbot! 🤖\n")

        elif user_input in ["what can you do", "help"]:
            print("Bot: I can chat with you! Try saying hello, how are you, etc.\n")

        elif user_input in ["bye", "goodbye", "exit"]:
            print("Bot: Goodbye! Have a great day! 👋\n")
            break

        else:
            print("Bot: Sorry, I don't understand that. Try 'hello' or 'how are you'!\n")

# Run the chatbot
chatbot()
def chatbot():
    print("Chatbot: Hello! I am your AI Chatbot.")
    print("Type 'bye' to exit.\n")
    while True:
        user = input("You: ").lower()
        if user in ["hello", "hi", "hey"]:
            print("Chatbot: Hello! How can I help you?")
        elif "how are you" in user:
            print("Chatbot: I am fine. Thank you!")
        elif "your name" in user:
            print("Chatbot: I am a simple AI Chatbot.")
        elif "course" in user:
            print("Chatbot: We offer courses in AI, Data Science, Python, and Machine Learning.")
        elif "college" in user:
            print("Chatbot: Welcome to the Engineering College Information System.")
        elif user in ["bye", "exit"]:
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            print("Chatbot: Sorry, I don't understand your question.")


chatbot()
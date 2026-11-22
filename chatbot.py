
print("====================================")
print("       WELCOME TO PYTHON BOT")
print("====================================")

print("Bot: Hello! I am Python Bot.")
print("Bot: You can ask me questions.")
print("Bot: Type 'bye' or 'exit' to end the conversation.")

while True:

    user = input("\nYou: ").lower().strip()

    # Greetings
    if "hello" in user or "hi" in user or "hey" in user:
        print("Bot: Hello! How are you?")

    elif "good morning" in user:
        print("Bot: Good morning! Have a great day.")

    elif "how are you" in user:
        print("Bot: I am fine. What about you?")

    # About chatbot
    elif "who are you" in user:
        print("Bot: I am a Python chatbot.")

    elif "what is your name" in user:
        print("Bot: My name is Python Bot.")

    elif "who created you" in user:
        print("Bot: I was created using Python.")

    elif "what is your job" in user:
        print("Bot: I am an intern as an Artificial Intelligence Engineer.")

    elif "which company" in user:
        print("Bot: I am working at a company named Pyrexia as an intern.")

    elif "what can you do" in user:
        print("Bot: I can answer simple questions about Python and AI.")

    # Python
    elif "what is python" in user:
        print("Bot: Python is a high-level programming language.")

    elif "what is programming" in user:
        print("Bot: Programming is the process of creating software.")

    # Artificial Intelligence
    elif "what is ai" in user or "artificial intelligence" in user:
        print("Bot: AI stands for Artificial Intelligence. It allows machines to perform tasks that normally require human intelligence.")

    elif "what is machine learning" in user or "machine learning" in user:
        print("Bot: Machine Learning is a subset of AI that allows systems to learn patterns from data.")

    elif "what is deep learning" in user or "deep learning" in user:
        print("Bot: Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers.")

    # General conversation
    elif "thank you" in user or "thanks" in user:
        print("Bot: You are welcome!")

    elif "good" in user:
        print("Bot: That's great!")

    elif "bad" in user:
        print("Bot: I hope things get better.")

    # Exit chatbot
    elif user == "bye" or user == "exit" or user == "quit":
        print("Bot: Goodbye! Have a nice day.")
        break

    # Unknown question
    else:
        print("Bot: Sorry, I don't understand. Can you ask something else?")


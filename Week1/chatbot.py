import string
print("="*50)
print("🤖 DecodeLabs Rule Based AI Chatbot")
print("="*50)
print("Type 'exit' anytime to quit")
print()
print("How can I help you today? ")
responses={
    "hello":"Hi there!",
    "hi": "Hello!",
    "hey": "Hey there!",
    "bye":"Goodbye!",
    "thanks":"You're Welcome!",
    "good morning":"Good Morning. Have a nice day!",
    "good afternoon": "Good Afternoon!",
    "good evening":"Good Evening!",
    "good night": "Good Night! Sleep well.",
    "who are you":"I am DecodeLab's AI Chatbot",
    "how are you":"I am doing well. Thank you for asking.",
    "what is python": "Python is an easy-to-learn programming language used in AI, web development, and many other applications.",
    "what is machine learning": "Machine Learning is a field of AI where computers learn patterns from data.",
    "what is chatbot": "A chatbot is a program designed to interact with users through text or conversation.",
    "what is your purpose": "I'm here to answer predefined questions and demonstrate a simple AI chatbot.",
    "tell me a joke":"Why do programmers prefer dark mode? Because light attracts bugs!",
    "who created you":"I was created by Pranathi as part of the DecodeLabs AI Internship.",
    "who made you": "I was created by Pranathi as part of the DecodeLabs AI Internship.",
    "help": """I can respond to:
            - hello
            - hi
            - hey
            - bye
            - thanks
            - good morning
            - good afternoon
            - good evening
            - good night
            - who are you
            - what is python
            - what is machine learning
            - what is chatbot
            - tell me a joke
            - who created you
            - exit"""

}
while True:
    user_input=input("You: ").strip().lower()
    user_input = user_input.translate(str.maketrans("", "", string.punctuation))
    if user_input=='exit':
        print("Bot: Goodbye. Have a nice day!")
        break
    response=responses.get(user_input,"Sorry, I don't understand that yet.")
    print(f"Bot: {response}")
    print()



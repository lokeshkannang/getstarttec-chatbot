from chatbot import chat_with_website

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = chat_with_website(user_input)
    print("Bot:", response)

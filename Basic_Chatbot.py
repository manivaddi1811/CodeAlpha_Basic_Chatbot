# ==========================================
# CodeAlpha Internship
# Task 3 : Basic Chatbot
# Developed by : Vaddi Manikanta
# ==========================================

from datetime import datetime

print("=" * 50)
print("        WELCOME TO PYTHON CHATBOT")
print("=" * 50)
print("Type 'bye' to exit the chatbot.\n")

while True:

    user = input("You : ").lower()

    if user == "hello" or user == "hi":
        print("Bot : Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot : I am doing great. How about you?")

    elif user == "what is your name":
        print("Bot : My name is Python Chatbot.")

    elif user == "who created you":
        print("Bot : I was created using Python programming.")

    elif user == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot : Current Time is", current_time)

    elif user == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot : Today's Date is", current_date)

    elif user == "help":
        print("\nBot : You can ask me:")
        print(" - hello")
        print(" - how are you")
        print(" - what is your name")
        print(" - who created you")
        print(" - time")
        print(" - date")
        print(" - bye")

    elif user == "bye":
        print("Bot : Thank you for chatting. Goodbye!")
        break

    else:
        print("Bot : Sorry, I don't understand that.")

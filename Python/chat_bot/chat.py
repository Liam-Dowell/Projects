#imports
import random
from logs import logs
from jokes import jokes as j
from calculator import addition as a
from calculator import subtraction as s
#======================

def chat_main():
    # chat_main accepts no arguements
    # it runs the main chat bot loop
    # it asks the user for input and responds accordingly

    # initilize user_input
    user_input = ""

    # output a welcome message and description of the use.
    print("Welcome to the Nasty Spider chat bot!")
    print("This is a friendly companion bot that will chat with you.")
    print("To exit the chat bot, say goodbye or bye.")
    while "bye" not in user_input:
        user_input = input(":> ") # Takes input from the user for what they want to chat about.
        user_input = user_input.lower()
        logs.create_logs(user_input)
        if "how are you" in user_input:
            print("I'm a robot, I don't feel anything.")
        elif user_input == "hello" or user_input == "hi":
            print("Hello user how can I help you today?")
        elif user_input == "what is your name":
            print("My name is Nasty Spider")
        elif "math" in user_input:
            math()
        elif "bye" in user_input:
            break
        else:
            print("I'm sorry, I don't understand.") 
            print("Ask me a different question.")
    goodbye()
    

def math():
    # user wanted help with math
    # math accepts no arguements
    # it propts the user for what they need help with
    i = 0
    total = 0
    print("")
    print("Sure I can help with math.")
    print("What do you need help with?")
    user_math = input(":> ")
    user_math = user_math.lower()
    if "add" in user_math or "plus" in user_math:
        a.addition()
    elif user_math == "subtraction" or user_math == "minus" or user_math == "i want to subtract numbers":
        s.subtract()
    
def goodbye():
    #goodbye accepts no arguements
    # it takes no input
    # it outputs a random goodbye
    goodbye_list = [
        "goodbye",
        "Adiós",
        "Au revoir",
        "Auf Wiedersehen",
        "Arrivederci",
        "Até logo",
        "さようなら",
        "再见",
        "안녕히 가세요",
        "До свидания",
        "Tot ziens"
    ]
    print(random.choice(goodbye_list))

chat_main()
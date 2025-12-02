import random
def chat_main():
    print("Welcome to the Nasty Spider chat bot!")
    print("This is a friendly comppanion bot that will chat with you.")
    print("To exit the chat bot, say goodbye or bye.")
    while user_input.lower() != "goodbye" and user_input.lower() != "bye":
        user_input = input("You: ")
        if "how are you" in user_input.lower():
            print("I'm a robot, I don't feel anything.")
        elif "what is your name" in user_input.lower():
            print("My name is Nasty Spider")
        elif "tell me a joke" in user_input.lower() or "give me a joke" in user_input.lower():
            joke = 0
            joke = random.randint(1, 3)
            if joke == 1:
                print("What do you call Mason Campbell?")
                filler = input(" ")
                print("Mason Campbell.")
                print("HAHAHAHAHAHAHA get it?")
            elif joke == 2:
                print("What do you call gage boyd?")
                filler = input(" " )
                print("Gage Boyd.")
                print("HAHAHAHAHAHA")
            elif joke == 3:
                print("I don't want to give you a joke.")
            else:
                print("There was an error while generating the integer.")
        else:
            print("I'm sorry, I don't understand.") 
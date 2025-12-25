#imports
import random
#========================
def give_joke():
    # user wanted a joke so i shall give them a joke
    # give_joke accepts no arguements
    # it reads from a text file called jokes.txt and randomly selects a joke to print to the user

    joke_list = []
    infile = open("/workspaces/Projects/Python/chat_bot/jokes/jokes.txt", "r")
    try:
        for line in infile:
            joke_list += [line.strip()]
        infile.close()
        print(random.choice(joke_list))
    except IndexError:
        print("I couldn't think of a joke to tell you.")
        print(" ")

def take_joke():
    # user wanted to tell me a joke so i shall use it for the next person
    # take_joke accepts no arguements
    # it propts the user for the joke
    print("Sure lets hear the joke.")
    user_joke = input(":> ")
    outfile = open("/workspaces/Projects/Python/chat_bot/jokes/jokes.txt", "a")
    outfile.write(user_joke + "\n")
    outfile.close()
    print("Thanks for the joke!")
    print("I think I'll save that joke for later.")
    print(" ")

import Number
import locks
import chat
def main():
    choice = 1
    while choice != 0:
        while choice < 1000 or choice > -1:
            print("Welcome to Projects main.")
            print("Specifically the python section.")
            print("What would you like to run today?")
            print("1) Number Guessing Game.")
            print("2) Locks")
            print("3) Chat Bot")
            print("0) QUIT")
            choice = int(input(":> "))
            if choice == 1:
                Number.number_guessing_main()
                break
            elif choice == 2:
                locks.lock_main()
                break
            elif choice == 3:
                chat.chat_main()
                break
            elif choice == 0:
                break
    print("GOODBYE")
    
main()
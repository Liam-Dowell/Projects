import Number
import locks
def main():
    choice = 1
    while choice != 0:
        print("Welcome to Projects main.")
        print("Specifically the python section.")
        print("What would you like to run today?")
        print("1) Number Guessing Game.")
        print("2) Locks")
        print("0) QUIT")
        choice = int(input(":> "))
        while choice < 3 or choice > -1:
            if choice == 1:
                Number.number_guessing_main()
                main()
            elif choice == 2:
                locks.lock_main()
                main()
    print("GOODBYE")
main()
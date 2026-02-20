def main():
    again = True
    while again == True:
        print("What would you like to do?")
        print("1. Give riddle")
        print("2. told a riddle")
        print("3. quit")
        choice = int(input(":> "))
        if choice == 1:
            give_riddle()
        if choice == 2:
            take_riddle()
        elif choice == 3:
            print("Auf weidersehen")
            again = False
        else:
            print("Error")

def give_riddle():
    inFile = open("/workspaces/Projects/Python/Riddle/the_riddler.txt", "a")
    print("What is your riddle?")
    riddle = input(":> ")
    print("What is the answer?")
    answer = input(":> ")
    inFile.write(riddle + '\n')
    inFile.write(answer + '\n')
    inFile.close()

def take_riddle():
    outFile = open("/workspaces/Projects/Python/Riddle/the_riddler.txt", "r")
    riddles = []
    answers = []
    riddle = outFile.readline()
    answer = outFile.readline()
    while riddle != ''




    
main()
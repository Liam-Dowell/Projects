import random

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
    inFile = open("the_riddler.txt", "a")
    print("What is your riddle?")
    riddle = input(":> ")
    print("What is the answer?")
    answer = input(":> ")
    inFile.write(riddle + '\n')
    inFile.write(answer + '\n')
    inFile.close()

def take_riddle():
    count = 0
    outFile = open("the_riddler.txt", "r")
    riddles = []
    answers = []
    riddle = outFile.readline()
    answer = outFile.readline()
    riddles.append(riddle)
    answers.append(answer)
    while riddle != '':
        riddle = outFile.readline()
        answer = outFile.readline()
        riddles.append(riddle)
        answers.append(answer)
        count += 1
    i = random.randint(1, count)
    riddle = riddles[i]
    answer = answers[i]
    print(riddle)
    print("What do you think the answer is?")
    user_answer = input(":> ")
    if user_answer == answer:
        print(f"Correct it was {answer}")
    else:
        print(f"Incorrect it was {answer}")

main()
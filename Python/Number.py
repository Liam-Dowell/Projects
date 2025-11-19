import random 
def number_guessing_main():
    again = "yes"

    while again == "yes" or again == "Yes":
        number = random.randint(1, 100)
        attempts = 1
        print ("Welcome to the Number Guessing Game.")
        print ("Im thinking of a number between 1 and 100.")
        guess = int(input("What is your first guess: "))
        while guess != number:
            while guess < 1001 and guess > 0:
                if guess > number:
                    print("To high.")
                    guess = int(input("Guess again: "))
                    attempts += 1
                elif guess < number:
                    print("To low.")
                    guess = int(input("Guess again: "))
                    attempts += 1
                else:
                    print("You got it correct.")
                    print(f"The number was {number}.")
                    print(f"It took you {attempts} tries.")
                    break
        print("Wanna play again?")
        again = input(":> ")




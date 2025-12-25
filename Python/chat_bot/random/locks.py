import random

def lock_main():
    min = 0
    max = 1
    i = 0
    print("This application generates possible lock combinations; assuming that the numbers will be from 0 to 9 (inclusive). Please first enter the quantity of dials on the combination locks. And then enter how many combinations you would like to generate.")
    number_of_dials = get_number_of_dials()
    number_of_locks = get_how_many_to_list()
    number = get_number(min, max)
    while i != number_of_locks:
        i += 1
        next_combo_number()

def get_number_of_dials():
    print("Each lock has how many dials?")
    number_of_dials = int(input(":> "))
    while number_of_dials < 3: 
        print("That is an invalid answer!")
        print("Please enter a valid answer on how many dials you want.")
        number_of_dials = int(input(":> "))
    return number_of_dials

def get_how_many_to_list():
    print("How many combinations should I generate?")
    number_of_locks = int(input(":> "))
    return number_of_locks

def get_number(min, max):
    number = random.randrange(10)
    return number

def next_combo_number():
    pass
    
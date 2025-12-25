def addition():
    #addition accepts no arguements
    #it asks the user for how many numbers they want to add
    #it then using a for loop asks the user for number and then which ever number they are on
    #it then outputs the results
    i = 1
    total = 0
    num_count = 0
    print("How many numbers are you adding?")
    num_count = int(input(":> "))
    for i in range(num_count):
        num = int(input(f"Number {i}: "))
        total += num
    print(f"The total is {total}")
    print(" ")
            
def subtract():
    print("What number are you subtracting?")
    num1 = int(input(":> "))
    num1 = total
    print(f"How many numbers are you subtracting from {num1}")
    num_count = int(input(":> "))
    for range in (1, num_count + 1):
        count += 1
        num2 = int(input(f"Number {count}: "))
        total -= num2
    print(f"The total is {total}.")
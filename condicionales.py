#!/usr/bin/env python3

while True: 
    print("Choose one of the following options: ")
    print("1. For Sum")
    print("2. For Substraction")
    print("3. For Multiplication")
    print("4. For Division")
    operation = int(input("Choose one of the options mentioned before or tipe -1 to quit the program: "))
    if operation != -1:
        if operation == 1:
            print("You choose to make a sum!")
            value1 = int(input("Enter the first value: "))
            value2 = int(input("Enter the second value: "))
            result = value1 + value2
            print("The result of your sum is: ", result)
        elif operation == 2:
            print("You choose to make a substraction!")
            value1 = int(input("Enter the first value: "))
            value2 = int(input("Enter the second value: "))
            result = value1 - value2
            print("The result of your substraction is: ", result)
        elif operation == 3:
            print("You choose to make a multiplication!")
            value1 = int(input("Enter the first value: "))
            value2 = int(input("Enter the second value: "))
            result = value1 * value2
            print("The result of your multiplication is: ", result)
        elif operation == 4:
            print("You choose to make a division!")
            value1 = int(input("Enter the first value: "))
            value2 = int(input("Enter the second value: "))
            result = value1 / value2
            print("The result of your division is: ", result)
        else:
            print("Please enter a valid choose")
    else:
        break

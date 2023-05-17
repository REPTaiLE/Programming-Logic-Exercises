#!/usr/bin/env python3

array = ""
loop = 1

while loop < 6:
    name = input("Give me a name out of 5: ")
    array += name 
    loop += 1
    if loop < 6:
        array += ", "
    else:
        break
print(array)
print("The program has ended")

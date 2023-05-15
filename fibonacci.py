#!/usr/bin/env python3
a = 0
b = 1
c = 0
number = int(input("Enter the number you want to stop the fibonacci sequence: "))

while c < number:
    c = a + b
    b = a
    a = c
    print(a, end=", ")

    

#!/usr/bin/env python3
counter = 1
name = input("Enter a name: ")
times = int(input("Enter a the times you want to print your name: "))
while True:
    if counter < times:
        print(name)
        counter += 1
    else: 
        break
        

#!/bin/python3
# A little bitty dice roller by a little bitty python programmer
# A mini-project for fun and no profit
# Created by Jake Herold
# If you're reading, utilizing, redistributing, or learning from this code you hearin agree to not judge my terrible code. 
#
# Version 0.0.1

# Modules
import random
import sys

# Remove program name from input and assign arguements to an array
program_name = sys.argv[0]
arguments = sys.argv[1:]

for arg in arguments:
    total = 0
    numberList = []
    for _ in range(int(arg.split('d')[0])):
        num = random.randint(1,int(arg.split('d')[1]))
        total += num
        numberList.append(num)
    print("Your " + arg + " results were: " + str(numberList))
    print("The total is: " + str(total) + "\n")

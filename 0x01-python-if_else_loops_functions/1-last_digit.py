#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

x = number % 10 if number > 10 else number % -10

if x > 5:
    message = "is greater than 5"
elif x == 0:
    message = "is 0"
elif x < 6 and x !=0:
    message = "is less than 6 and not 0"

print(f"Last digit of {number} is {x} and {message}")

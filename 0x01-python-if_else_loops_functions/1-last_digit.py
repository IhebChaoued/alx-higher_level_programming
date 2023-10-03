#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

x = number % 10

if x > 5:
    message = "is greater than 5"
elif x == 0:
    message = "is 0"
else:
    message = "and is less than 6 and not 0"

print(f"Last digit of {number} is {x} and {message}")

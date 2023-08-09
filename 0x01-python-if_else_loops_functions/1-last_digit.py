#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    print (f"{number} is greater than five")
elif number < 6:
    print (f"{number} is negative")
else:
    print (f"{number} is zero")

import random

name = input("what's your name? ")
print(name)
name = "Hello " + name + " welcome to math test. Good luck!"
print(name)

num1 = random.randint(1,10)
num2 = random.randint(1,10)
op = "+"

q = "what is " + str(num1) + op + str(num2) + "? "
print(q)
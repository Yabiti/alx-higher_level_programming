import random
name = input("what's your name? ")

welcome_message = "hello " + name + " welcome to math test Good Luck!"
print(welcome_message)

num1 = random.randint(1, 5)
num2 = random.randint(1, 5)
op = "+"

q = "what is " + str(num1) + op + str(num2) + "? "
print(q)
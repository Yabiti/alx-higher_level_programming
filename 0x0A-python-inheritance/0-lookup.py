import random
def greet_user(user_name):
    welcome_message = "Hello " + user_name + " Welcome to math test"
    print(welcome_message)

def print_question(num1, num2, op):
    q = "what is " + str(num1) + op + str(num2) + "? "
    print(q)
def print_result(user_name):
    farewell_message = farewell_message = "thanks for taking this quiz" + user_name + "Your score is" + str(score) + "out of 5"
    print(farewell_message)

def choose_operator(op_n):
    if op_n == 1:
        return "+"
    elif op_n == 2:
        return "-"
    elif op_n == 3:
        return "*"
    elif op_n == 4:
        return "/"
    else:
        return "invalid operator"

def calculate_answer(n1, n2 , op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2
    else:
        return "invalid operator"

user_name = input("what's your name? ")

greeting = greet_user(user_name)

score = 0
total = 0

while total < 5:

    num1 = random.randint(1,10)
    num2 = random.randint(1,10)

    op_num = random.randint(1,4)
    op = choose_operator(op_num)

    print_question(num1, num2 , op)
    user_answer = input("Ans: ")
    correct_answer = calculate_answer(num1, num2, op)

    if user_answer == correct_answer:
        print("Correct answer: ")
        score = score + 1
    else:
        print("oops wrong answer", correct_answer)

        total = total + 1

print_result(user_name, score)
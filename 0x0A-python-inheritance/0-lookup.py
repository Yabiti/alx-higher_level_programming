def greet_user(user_name):
    farewell_message = "Hello " + user_name + " Welcome to math test"
    print(farewell_message)

def print_question(num1, num2, op):
    q = "what is " + str(num1) + op + str(num2) + "? "
    print(q)

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

def calculate_question(n1, n2 , op):
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
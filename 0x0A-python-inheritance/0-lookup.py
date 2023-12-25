def greet_user(user_name):
    welcome_messsage = "Hello " + user_name + "welcome to math test"
    print(welcome_messsage)

def print_qusetion(num1, num2 ,op):
    q = "what is " + str(num1) + op + str(num2) + "? "
    print(q)

def print_result(user_name, score):
    farewell_message = farewell_message = "thanks " + user_name + "your score is" + str(score) + "out of 5"
    print(farewell_message)

def choose_opretator(op_n):
    if op_n == 1:
        return "-"
    elif op_n == 2:
        return "+"
    elif op_n == 3:
        return "*"
    elif op_n == 4:
        return "/"
    else:
        return "invalid operator"

def calculate_answer(n1, n2 , op):
    if op == "-":
        return n1 - n2
    
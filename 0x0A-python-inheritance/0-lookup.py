def greet_user(user_name):
    farewell_message = "Hello " + user_name + " Welcome to math test"
    print(farewell_message)

def print_question(num1, num2, op):
    q = "what is " + str(num1) + op + str(num2) + "? "
    print(q)

def calculate_question(op_num):
    if op_num == 1:
        return "+"
    if op_num == 2:
        return "-"
    
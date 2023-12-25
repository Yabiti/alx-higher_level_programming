def greet_user(user_name):
    welcome_message = "hello" + user_name + "welcome to math test Good Luck!"
    print(welcome_message)

def choose_operator(op_n):
    if op_n == 1:
        return "-"
    elif op_n == 2:
        return "+"
    elif op_n == 3:
        return "*"
    elif op_n == 4:
        return "/"

def greet_user(user_name):
    welcome_message = "hello" + user_name + "welcome to math test Good Luck!"
    print(welcome_message)

def print_question(num1, num2, op):
    q = "what is " + str(num1) + op + str(num2) + "? "
    print(q)

def choose_operator(op_n):
    if op_n == 1:
        return "_"
    if op_n == 2:
        return "+"
    if op_n == 3:
        return "*"
    if op_n == 4:
        return "/"
def print_result(user_name):
    farewell_message = "thanks for taking this test" +  user_name + "we'll send your result soon"
    print(farewell_message)
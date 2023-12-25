import random
def greet_user(user_name):
    welcome_message = "hello" + user_name + "welcome to math test Good Luck!"
    print(welcome_message)

def print_question(num1, num2, op):
    q = "what is " + str(num1) + op + str(num2) + "? "
    print(q)

def choose_operator(op_n):
    if op_n == 1:
        return "_"
    elif op_n == 2:
        return "+"
    elif op_n == 3:
        return "*"
    elif op_n == 4:
        return "/"
    else:
        return "invalid oprator"
def print_result(user_name):
    farewell_message = "thanks for taking this test" +  user_name + "we'll send your result soon"
    print(farewell_message)
user_name = input("please enter your name ")
greet_user(user_name)

num1 = random.randint(1,10)
num2 = random.randint(1,10)
op = "+"

print_question(num1 , num2 , op)
user_answer = input("Ans: ")
correct_answer = num1 + num2
print("your answer is ", user_answer)
print("The correct answer is ", correct_answer)

num1 = random.randint(1,10)
num2 = random.randint(1,10)
op_num = random.randint(1,4)
op = choose_operator(op_num)
user_answer = input("Ans: ")
correct_answer = num1 - num2
print("Ypur answer is ", user_answer)
print("the correct answer is ", correct_answer)

num1 = random.randint(1,10)
num2 = random.randint(1,10)
op = "*"
user_answer = input("Ans: ")
correct_answer = num1 * num2
print("your answer is", user_answer)
print("the correct anwer is ", correct_answer)

num1 = random.randint(1,10)
num2 = random.randint(1,10)
op = "*"
user_answer = input("Ans: ")
correct_answer = num1 * num2
print("your answer is", user_answer)
print("the correct anwer is ", correct_answer)

num1 = random.randint(1,10)
num2 = random.randint(1,10)
op = "*"
user_answer = input("Ans: ")
correct_answer = num1 * num2
print("your answer is", user_answer)
print("the correct anwer is ", correct_answer)

num1 = random.randint(1,10)
num2 = random.randint(1,10)
op = "*"
user_answer = input("Ans: ")
correct_answer = num1 * num2
print("your answer is", user_answer)
print("the correct anwer is ", correct_answer)


num1 = random.randint(1,10)
num2 = random.randint(1,10)
op = "/"
user_answer = input("Ans: ")
correct_answer = num1 / num2
print("your answer is", user_answer)
print("the correct anwer is ", correct_answer)

print_result(user_name)
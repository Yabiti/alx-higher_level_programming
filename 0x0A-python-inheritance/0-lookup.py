def print_question(num1 , op , num2):
    print()
    q = "what's is " + str(num1) + op + str(num2) + "? "
    print(q)
def answer_feedback(user_ans, correct_ans):
    print("user's answer is: ", user_ans)
    print("correct_answer is: ", correct_ans)

n1 = 5
n2 = 10
print_question(n1, "+", n2)
user_ans = input("Ans ")
correct_ans = n1 + n2
answer_feedback(user_ans, correct_ans)

print_question(n1, "-", n2)
user_ans = input("Ans ")
correct_ans = n1 - n2
answer_feedback(user_ans, correct_ans)

print_question(n1, "*", n2)
user_ans = input("Ans ")
correct_ans = n1 * n2
answer_feedback(user_ans, correct_ans)

print_question(n1, "/" ,n2)
user_ans = input("Ans ")
correct_ans = int(n1 / n2)
answer_feedback(user_ans, correct_ans)

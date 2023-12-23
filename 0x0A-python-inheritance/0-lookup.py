n1 = 4
n2 = 7

q = "what is " + str(n1) + "+" + str(n2) + "? "
user_answer = input(q)
print("user_answer", user_answer)
correct_answer = n1 + n2
print("correct_answer", correct_answer)

q = "what is " + str(n1) + "-" + str(n2) + "? "
user_answer = input(q)
print("user_answer", user_answer)
correct_answer = n1 - n2
print("correct_answer", correct_answer)
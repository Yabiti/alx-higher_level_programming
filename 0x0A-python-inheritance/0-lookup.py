score = 0
first_name, Last_name = input("what's your name? ")
print("hello", first_name + Last_name, "welcome to maths test")
print('be fucking  ready')

user_answer = input("what's 6 + 7 ")
print("user_answer", user_answer)
correct_answer = 6 + 7
print("correct_answer", correct_answer)


user_answer = input("what's 6 - 7 ")
print("user_answer", user_answer)
correct_answer = 6 - 7
print("correct_answer", correct_answer)


user_answer = input("what's 6 * 7 ")
print("user_answer", user_answer)
correct_answer = 6 * 7
print("correct_answer", correct_answer)


user_answer = input("what's 6 / 7 ")
print("user_answer", user_answer)
correct_answer = 6 / 7

print("correct_answer", correct_answer)
if correct_answer == user_answer:
    score = score + 1
print("score", score)
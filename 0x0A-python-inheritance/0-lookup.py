score = 0
name = input("what's your name? ")
print("hello", name, "welcome to maths test")

user_answer = input("what's 6 + 7 ")
print("user_answer", user_answer)
correct_answer = 6 + 7
print("correct_answer", correct_answer)
if correct_answer == user_answer:
    score = score + 1
    print("score", score)
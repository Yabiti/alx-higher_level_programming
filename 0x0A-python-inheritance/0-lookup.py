score = 0
print("your score is", score)
user_answer = int(input("what's 5 * 6? "))
correct_answer = 5 * 6
if user_answer == correct_answer:
    score = score + 1
    print("great your new score is:", score)
else:
    print("badly it's a wrong answer")
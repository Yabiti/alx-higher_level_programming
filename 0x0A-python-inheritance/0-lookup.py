def main():
    print("this is main function")
    condtional_exec()
    conditional_values()
def conditional_exec():
    a, b = 1 , 3
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")
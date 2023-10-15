def main():
    print("this is main function")
    conditional_exec()
    conditional_values()


def conditional_exec():
    a, b = 1 , 3
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")

def conditional_values():
    a , b = 1 , 2
    statements = "less than" if a < b else "not less than"
    print(statements)

if __name__ == "__main__":
    main()
def main():
    conditional_exec()
    conditional_values()

def conditional_exec():
    a, b = 2, 2
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")

def conditional_values():
    a , b = 1 , 2
    statements = "is less than" if a < b else "not less than"
    print(statements)

if __name__ == "__main__":
    main()

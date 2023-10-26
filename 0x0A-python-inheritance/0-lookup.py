#!/usr/bin/python3

def main():
    conditional_exec()


def conditional_exec():
    a,b = 1,2
    if a < b:
        print("a is lessthan b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equak to b")

if __name__ == "__main__":
    main()
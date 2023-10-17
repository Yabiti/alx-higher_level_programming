#!/usr/bin/python3

def main():
    PassingParameters(1,12)

def PassingParameters(argument1, argument2 = None, argument3 = 6):
    if argument2 == None:
        print("here is our arguments:", argument1, argument2, argument3)
    else:
        print("here is our arguments:", argument1, argument2, argument3)

if __name__ == "__main__":
    main()
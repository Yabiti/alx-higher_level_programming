#!/usr/bin/python3

def main():
    PassingParameters(1,4,6)

def PassingParameters(argument1, argument2 = 4, argument3 = 6):
    print("here is our arguments:", argument1, argument2, argument3)

if __name__ == "__main__":
    main()
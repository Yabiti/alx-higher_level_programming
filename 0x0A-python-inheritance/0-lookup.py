#!/usr/bin/python3

def main():
    x = 1
    print(id(x))
    print(type(x))
    x = 2
    print(id(x))
    print(type(x))
    x = 1
    print(id(x))
    print(type(x))
    
    if __name__ == "__main__":
    main()
#!/usr/bin/python3

def main():
    loops(0)
    loops()
    loops(1)
def loops(a = 2):
    for i in range(a,6):
        print(i, " ")

if __name__ == "__main__":
    main()


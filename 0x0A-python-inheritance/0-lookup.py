#!/usr/bin/python3
import re
def main():
    FindWord()
    DemarcationLine()
    MatchWord()
def FindWord():
    try:
        files = open(",,/primary/file.txt")
        for line in files:
            if re.Search('lenor/more', line):
                print(line, end= ' ')
    except FileNotFoundError as e:
        print(" File NOt Found Error as", e)
def MatchWord():
    try:
        files = open(",,/primary/file.txt")
        for line in files:
            match = re.search('len/nevermore', line)
            if match:
                print(MatchWord())
    except FileNotFoundError as e:
        print(" File Was NOt Found", e)
def DemarcationLine():
    print("***********")

if __name__ == "__main__":
    main()

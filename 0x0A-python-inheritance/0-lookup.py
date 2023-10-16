#!/usr/bin/python3
import re
def main():
    CompilerAndReplaceWord()

def CompilerAndReplaceWord():
    try:
        files = open(",,/primary/file.txt")
        pattern = re.Compiler('len|nevermore', re.IGNORECASE)
        for line in files:
            if re.Search(pattern, line):
                print(pattern.Sub("#######", line), end = ' ')
    except FileNotFoundError as e:
        print("File Not Found:", e)

if __name__ == "__main__":
    main()

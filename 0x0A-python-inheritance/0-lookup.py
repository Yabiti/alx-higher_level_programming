name = input("what's your name? ").rstrip().title()

first, last = name.split(" ")
print(f"hello, {first}")
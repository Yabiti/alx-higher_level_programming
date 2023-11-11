def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("what's the n? "))
        if n > 0:
            return n
def meow(n):
    print("meow")

main()
def main():
    number = get_number()
    meow()

def get_number():
    while True:
        n = int(input("what's the number? "))
        if n > 0:
            return n
def meow(n):
    for _ in range(n):
        print("meow")
main()
def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("Even")
    else:
        print("odd")

def is_even(n):
    
    if n % 2 == 0:
        return True
    else:
        return False
main()
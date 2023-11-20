 # Sposob 1

x = int(input("Whats x?"))
if x % 2== 0:
    print("X is even")
else:
    print("X is odd")

# Obiektowo
def main():
    x = int(input("Whats x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n% 2 == 0 else False
    # return n % 2 == 0
    
main()
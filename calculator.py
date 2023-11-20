def main():
    x = int (input("Whats x?"))
    print("x squared is", square(x))
    
def square(n):
    return pow(n,2)

main()

x = int(input("Whats x?"))
y = int(input("Whats y?"))
z = round(x +y)
print(x +y)
print(f"{z:,}")
#You can also write
print(int(input("Whats x?")) + int(input("Whats y?")))

z = (x/y)
print (f"{z:.2f}")
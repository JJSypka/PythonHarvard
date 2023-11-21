# Syntax error - "literówki"
# Value error - "iteruje stringa np"
# Name error - doing sth with a variable that u shoudn't
try:
    x = int (input("Whats x?"))
except ValueError:
    print("X is not an integer")
else:    
    print(f"x is {x}")
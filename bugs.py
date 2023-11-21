# Syntax error - "literówki"
# Value error - "iteruje stringa np"
# Name error - doing sth with a variable that u shoudn't
def main():
    x = get_int()
    
def get_int():
    while True:
        try:
            return int (input("Whats x?"))
        except ValueError:
            pass
        


main()
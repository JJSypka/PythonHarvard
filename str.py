name = input("Whats your name?")

# Remove white space from str
name = name.strip()

#Capitalize user's name - just 1st letter
name = name.capitalize()

#Capitalize - first letters on every word
name = name.title()

#It can be in 1 line
name = name.strip().title()

#Or the easiest
name = input("Whats your name?").strip().title()
print(f"hello, {name}")

#Split user name untoi first name and last name
name = input("Whats your name?")
first, last = name.split(" ")
print(f"Hello, {first}")



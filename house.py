name = input("Whats  your name?")


match name:
    case "Harry" | "Hermione" | "Ron ":
        print("Griffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Who?")
        
        
if name == "Harry" or name == "Hermione" or name =="Ron":
    print("Griffindor")
elif name == "Draco":
    print("slytherin")
else:
    print("Who?") 
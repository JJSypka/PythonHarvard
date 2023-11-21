students = [ "Harry","Hermione", "Ron"]
houses = ["Griffindor","Griffindor","Griffindor","Slytherin"]
for student in students:
    print(student)
for i in range(len(students)):
    print (i + 1,students[i])
    
students= {
    "Hermione":"Griffindor",
    "Harry": "Griffindor",
    "Ron":"Griffindor",
    "Draco":"Slytherine",
}

students = [
    {"name": "Hermione","house": "Gryffindor","patronus": "Otter"},
    {"name": "Harry","house": "Gryffindor","patronus": "Stag"},
    {"name": "Ron","house": "Gryffindor","patronus": "Jack Russel terrier"},
    {"name": "Draco","house": "Slytherin","patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
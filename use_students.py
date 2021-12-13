from typing import Union
from students import Students
# Defining a function for building a Record which generates list of all the students
def Markss(rec, name, roll, marks):
    rec.append(Students(name, roll, marks))
    return rec

Record = []
number_of_students = "y"
while number_of_students == "y":
    name = input("Enter the name of the student: ")
    if not isinstance(name, str):
        raise TypeError("Name must be a string")

    height = input("Enter the roll number: ")
    roll = input("Marks: ")
    Record = Markss(Record, name, roll, height)
    number_of_students = input("Another student? y/n: ")

# Printing the list of student
n = 1
for el in Record:
    print(n, '. ', el)
    n = n + 1
# •	4. Implement a `Student` class with a constructor that initializes 
# `name` and `roll_number`. Write a method to return student details.
class Student:
    def __init__(self,name:str,roll_number:str):
        self.name=name
        self.roll_number=roll_number

    def studentDetails(self):
        print(f"Student name is {self.name} and roll number is {self.roll_number}.")


name,roll_number=map(str,input("Enter name and roll number of the student: ").split())
student1=Student(name,roll_number)

student1.studentDetails()
students=[]
class student:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
    def getDetails(self)->float:
        return self.age
        # return 

def getInput():
    n=int(input("Enter number of students: "))
    for i in range(n):
        name,age=map(str,input("Enter name and age: ").split()) 
        students.append(student(name,age))

def main():
    getInput()

    for i in students:
        print(i.getDetails(),type(i.getDetails()))

main()
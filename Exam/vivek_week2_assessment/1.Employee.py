# •	1. Create a class `Employee` with properties `name`, `id`, and `department`. 
# Instantiate an object and assign values dynamically.
class Employee:
    def __init__(self,name:str,id:int,department:str)->None:
        self.name=name
        self.id=id
        self.department=department

    def EmployeeDetails(self)->None:
        print(f"Employee name is {self.name} ({self.id}) from {self.department}.")

name,id,department=map(str,input().split())
emp1=Employee(name,id,department)

emp1.EmployeeDetails()

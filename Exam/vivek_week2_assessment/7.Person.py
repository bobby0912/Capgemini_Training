# •	7. Create a multi-level class structure with `Person` → `Employee` → `Manager`, where `Manager` 
# has an additional method `approve_leave()`.
class Person:
    def __init__(self,name:str):
        self.name=name
    def personDetails(self):
        print(f"name : {self.name}")

class Employee(Person):
    def __init__(self, name,employee_id):
        super().__init__(name)
        self.employee_id=employee_id

    def EmployeeDeails(self):
        super().personDetails()
        print(f"id : {self.employee_id}")

class Manager(Employee):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)

    def ManagerDetails(self):
        super().EmployeeDetails()

    def approve_leave(self):
        print("leave is approved.")

name,id=map(str,input("enter name and id if the manager: ").split())
manager1=Manager(name,id)
manager1.approve_leave()




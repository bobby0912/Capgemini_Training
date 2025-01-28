class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def displayInfo(self):
        print(f"this car os a {self.brand} {self.model}")

car1=car('toyota','innova')
car2=car('honda','civic')

# car1.displayInfo()
# car2.displayInfo()

class Employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary

    def setSalary(self,salary):
        self.__salary=salary
    def getSalary(self)->bool:
        return self.__salary
    def totalSalary(self,deductions,allowances):
        return self.__salary-deductions+allowances

name,salary=map(str,input("enter name and salary: ").split())
emp=Employee(name,int(salary))
print("salary before update: ",emp.getSalary())

emp.setSalary(6000)

print("salary After update: ",emp.getSalary())

deductions,allowances=map(int,input("Enter deductions and allowances: ").split())
print("final salary: ",emp.totalSalary(deductions,allowances))















# class 
#     employee name 
#     id
#     age
#     salary
#     designation
#     experience

#     getDetails()


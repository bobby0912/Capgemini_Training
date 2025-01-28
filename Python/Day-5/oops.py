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
        self.__deductionsList=[]
        self.__allowancesList=[]

    def setSalary(self,salary):
        self.__salary=salary

    def getSalary(self):
        return self.__salary

    def salaryDeductions(self,deduction):
        self.__deductionsList.append(deduction)
        # __salary-=deduction

    def salaryAllowances(self,allowances):
        self.__allowancesList.append(allowances)
        # __salary+=allowances

    def totalSalary(self,allowances):
        return self.__salary+sum(self.__allowancesList)-sum(self.__deductionsList)

name,salary=map(str,input("enter name and salary: ").split())
emp=Employee(name,int(salary))
# print("salary before update: ",emp.getSalary())

# emp.setSalary(6000)

# print("salary After update: ",emp.getSalary())

# deductions,allowances=map(int,input("Enter deductions and allowances: ").split())
# print("final salary: ",emp.totalSalary(deductions,allowances))

tax1=int(input("Enter tax that deducted: "))
emp.salaryDeductions(tax1)

tax2=int(input("Enter tax that deducted: "))
emp.salaryDeductions(tax2)

allowance1=int(input("Enter the allowances: "))
emp.salaryAllowances(allowance1)

print("Final salary: ",emp.getSalary())



















# class 
#     employee name 
#     id
#     age
#     salary
#     designation
#     experience

#     getDetails()


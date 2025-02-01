# •	2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods. 
# Implement logic to prevent overdraft.
class BankAccount:
    def __init__(self,balance:int)->None:
        self.__balance=balance
    def getBalance(self)->str:
        return f"your balance is {self.__balance}"
    def deposit(self,amount:int)->None:
        self.__balance+=amount
        print("Deposit Successful.")
    def withdraw(self,amount:int)->None:
        if(amount>self.__balance):
            print("Low balance, cannot withdraw")
        else:
            self.__balance-=amount
            print("Withdraw successful.")
        
user=BankAccount(1000)
# print(user.__balance) gives error because private member variable we cannot modify
print(user.getBalance())

user.deposit(500)
print(user.getBalance())

user.withdraw(250)
print(user.getBalance())

user.withdraw(2000)
print(user.getBalance())



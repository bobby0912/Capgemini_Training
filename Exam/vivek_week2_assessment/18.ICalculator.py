# •	18. Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`. 
# Create a `BasicCalculator` class that implements these methods.
from abc import ABC,abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def subtract(self):
        pass
    @abstractmethod
    def multiply(self):
        pass
    @abstractmethod
    def divide(self):
        pass

class BasicCalculator(ICalculator):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    def multiply(self):
        print(self.a*self.b)
    def subtract(self):
        print(self.a-self.b)
    def divide(self):
        print(self.a/self.b)

a,b=map(int,input("Enter two numbers: ").split())
calculation=BasicCalculator(a,b)
calculation.add()
calculation.subtract()
calculation.multiply()
calculation.divide()
        
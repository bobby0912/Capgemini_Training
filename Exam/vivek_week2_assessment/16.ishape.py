# •	16. Create an interface `IShape` with an abstract method 
# `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.
from abc import ABC,abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculareArea(self):
        pass

class Rectangle(IShape):
    def __init__(self,length:int,breadth:int):
        self.length=length
        self.breadth=breadth
    def calculareArea(self):
        print(f"The area of the rectangle is {self.length*self.breadth}")

class Circle(IShape):
    def __init__(self,radius:int):
        self.radius=radius
    def calculareArea(self):
        print(f"The area of the rectangle is {3.14*self.radius**2}")

length,breadth=map(int,input("Enter length and breadth of the rectangle: ").split())
rectangle1=Rectangle(length,breadth)
rectangle1.calculareArea()

radius=int(input("Enter the radius of the circle: "))
circle1=Circle(radius)
circle1.calculareArea()
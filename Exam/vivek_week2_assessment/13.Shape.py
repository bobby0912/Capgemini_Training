# •	13. Develop a `Shape` class with a method `area()`. 
# Implement `Square` and `Triangle` classes that provide 
# specific implementations for `area()`.
class Shape:
    def area(self):
        print("This method is used to print the area of the shape.")

class Square(Shape):
    def __init__(self,side:int):
        self.side=side
    def area(self):
        print(f"The area of the square is {self.side**2}")

class Triangle(Shape):
    def __init__(self,base:int,height:int):
        self.base=base
        self.height=height
    def area(self):
        print(f"the area of the triangle is {0.5*self.base*self.height}")


square1=Square(4)
square1.area()

triangle1=Triangle(10,20)
triangle1.area()
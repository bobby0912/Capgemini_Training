# •	6. Implement a multi-level inheritance example where `Vehicle` is a base class,
# `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.
class Vehicle:
    def displayTree(self):
        return "Vehicle"

class Car(Vehicle):
    def displayTree(self):
        return super().displayTree()+" -> Car"

class Bike(Vehicle):
    def displayTree(self):
        return super().displayTree()+" -> Bike"

class ElectricCar(Car):
    def displayTree(self):
        return super().displayTree()+" -> Electric car"


car1=Car()
print(car1.displayTree())#Vehicle -> Car

bike1=Bike()
print(bike1.displayTree())#Vehicle -> Bike

electricCar=ElectricCar()
print(electricCar.displayTree())#Vehicle -> Car -> Electric car
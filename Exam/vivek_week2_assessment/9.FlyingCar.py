# •	9. Simulate multiple inheritance where `FlyingCar` inherits 
# from both `Car` and `Airplane`. Handle potential conflicts in the `move()` method.

class Car:
    def move(self):
        print("Car moves on Wheels.")

class Airplane:
    def move(self):
        print("Airplane flies in air")

class FlyingCar(Car,Airplane):
    def move(self):
        # Car.move(self)
        # Airplane.move(self)
        print("Flying car can go by wheels and in air.")
    
flyingcar1=FlyingCar()
flyingcar1.move()
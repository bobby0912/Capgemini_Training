# •	19. Develop an interface `IVehicle` with abstract methods `start_engine()` and `stop_engine()`. 
# Implement it in `Car`, `Bike`, and `Truck` classes.
from abc import ABC,abstractmethod

class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass

class car(IVehicle):
    def start_engine(self):
        print("Car engine is started.")
    def stop_engine(self):
        print("car engine is stopped.")
class Bike(IVehicle):
    def start_engine(self):
        print("Bike engine is started.")
    def stop_engine(self):
        print("Bike engine is stopped.")
class Truck(IVehicle):
    def start_engine(self):
        print("Truck engine is started.")
    def stop_engine(self):
        print("Truck engine is stopped.")

car1=car()
car1.start_engine()
car1.stop_engine()

bike1=Bike()
bike1.start_engine()
bike1.stop_engine()

truck1=Truck()
truck1.start_engine()
truck1.stop_engine()

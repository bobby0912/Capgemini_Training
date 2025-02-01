# •	10. Build a `SmartPhone` class inheriting from `MobileDevice`, 
# which in turn inherits from `Electronics`.
#  Demonstrate method overriding and attribute reuse.
class Electronics:
    def __init__(self,companyName):
        self.companyName=companyName
    def display(self):
        print(f"the product belongs to {self.companyName}")

class MobileDevice(Electronics):
    def __init__(self, companyName,brand):
        super().__init__(companyName)
        self.brandName=brand
    def display(self):
        super().display()
        print(f"This product is form {self.brandName} brand.")

class SmartPhone(MobileDevice):
    def __init__(self, companyName, brand,name):
        super().__init__(companyName, brand)
        self.name=name
    def display(self):
        super().display()
        print(f"this phone name is {self.name}")


smartphone1=SmartPhone("Pixel 7a","Google","Google")
smartphone1.display()
# print(smartphone1.companyName)
# a=MobileDevice()
# print(a.companyName)


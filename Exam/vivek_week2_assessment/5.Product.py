# •	5. Create a `Product` class with attributes `name`, `price`, and `stock`. 
# Write a method `check_availability(quantity)` that returns 
# whether the requested quantity is available.
class Product:
    def __init__(self,name:str,price:int,stock:int)->None:
        self.name=name
        self.price=price
        self.stock=stock

    def check_availability(self,quantity):
        if(self.stock>=quantity):
            print("Stock available.")
        else:
            print("Running out of Stock.")

name=input("Enter name of the product: ")
price,stock=map(int,input("Enter price and stock: ").split())
product1=Product(name,price,stock)

quantity=int(input("Enter quantity to check availability: "))
product1.check_availability(quantity)
        
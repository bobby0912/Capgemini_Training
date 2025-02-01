# •	8. Design a system where a base class `Animal` has a 
# method `speak()`, and subclasses `Dog` and `Cat` override it.
class Animal:
    def speak(self):
        print("Animal can speak.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

class Cat(Animal):
    def speak(self):
        print("cat meow.")

dog1=Dog()
dog1.speak()

cat1=Cat()
cat1.speak()

# class Cat:
#     def sound(self):
#         print("meow.")

# class Dog:
#     def sound(self):
#         print("Bark.")

# for i in [Cat(),Dog()]:
#     i.sound(i)

class example:
    static_var=1
    def __init__(self):
        example.static_var+=1
        print(example.static_var)

p1=example()
p2=example()
p3=example()

print(p3.static_var)
example.static_var=50
print(p3.static_var)

p4=example()


# class cat
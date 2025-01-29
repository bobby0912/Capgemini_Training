class Bird:
    def fly(self):
        return "this bird can fly."
    
class Mamal:
    def walk(self):
        return "this mamal can walk."
    
class Bat(Bird,Mamal):
    def dance(self):
        return "huhu"
    
bat=Bat()
print(bat.fly())
print(bat.walk())

m1=Mamal()
# print(m1.dance())
# m1=bat
print(m1.dance())

b2=Bat()

b2=m1
print(b2.dance())


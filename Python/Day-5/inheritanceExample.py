class Parent:
    def __init__(self):
        self.bigNose="7cm"
    def displayParent(self):
        print("this is a parent class.")

class Child(Parent):
    def __init__(self):
        # print("child constructor")
        super().__init__()
    def displayChild(self):
        print("This is a child class.")
    
# c1=Child()
# c1.displayChild()
# # Parent.display(c1)
# print(c1.bigNose)
# c1.displayParent()

# p1=Parent()
# p1.display_parent()
# p1.display_child()


class School:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def display(self):
        print(self.name,self.gender,sep="\n",end=" ")
    
class College(School):
    def __init__(self, name, gender,domain):
        super().__init__(name, gender)
        self.domain=domain
    def display(self):
        super().display()
        print(self.domain)

class PostGrad(College):
    def __init__(self, name, gender,domain,projectName):
        super().__init__(name, gender,domain)
        self.projectName=projectName
    def display(self):
        super().display()
        print(self.projectName)

name,gender,domain,projectName=map(str,input("Enter name,gender,domain,projectName: ").split())
student=PostGrad(name,gender,domain,projectName)
student.display()



    
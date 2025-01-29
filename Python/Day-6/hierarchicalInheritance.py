class shape:
    def __init__(self):
        print("shape constructor.")
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2

class square(shape):
    def __init__(self,side):
        super().__init__()
        self.side=side

    def area(self):
        return self.side**2

c=circle(10)
print(c.area())

s=square(10)
print(s.area())
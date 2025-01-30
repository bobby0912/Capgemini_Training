from abc import ABC,abstractmethod
class father(ABC):
    @abstractmethod
    def display(self):
        pass
    def panCard(self):
        print("456543")

class child(father):
    def display(self):
        super().display()
        print("this is a child class.")
    def panCard(self):
        print('898789')

c1=child()
c1.display()

# f1=father()
# f1.panCard()

c1.panCard()
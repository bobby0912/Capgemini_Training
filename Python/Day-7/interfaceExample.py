from abc import ABC,abstractmethod
class inter_face(ABC):
    @abstractmethod
    def abs_method(self):
        pass

class child(inter_face):
    def abs_method(self):
        print("child class method.")

c1=child()
c1.abs_method()
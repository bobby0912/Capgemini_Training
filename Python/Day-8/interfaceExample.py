from abc import ABC,abstractmethod

class Mail(ABC):
    @abstractmethod
    def send(self):
        pass 

class Email(Mail):
    def send(self):
        print("Email class")

class SMS(Mail):
    def send(self):
        print("SMS class")

class Whatsapp(Mail):
    def send(self):
        print("Whatsapp class")

e1=Email()
e1.send()

s1=SMS()
s1.send()

w1=Whatsapp()
w1.send()


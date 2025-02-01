# •	20. Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` 
# methods, and it is implemented by `GoogleAuth` and `FacebookAuth` classes.
from abc import ABC,abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self):
        print("Logged in through google")
    def logout(self):
        print("logged out from google")

class FacebookAuth(UserAuthentication):
    def login(self):
        print("Logged in through Facebook")
    def logout(self):
        print("logged out from Facebook")


googleauth1=GoogleAuth()
googleauth1.login()
googleauth1.logout()

facebookauth1=FacebookAuth()
facebookauth1.login()
facebookauth1.logout()
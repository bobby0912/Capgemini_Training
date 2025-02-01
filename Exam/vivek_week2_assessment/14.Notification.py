# •	14. Implement method overriding for a `Notification` class 
# where `send()` is overridden in `EmailNotification` and `SMSNotification`.
class Notification:
    def send(self):
        print("notification has been sent.")

class EmailNotification(Notification):
    def send(self):
        print("Email has been sent.")

class SMSNotification(Notification):
    def send(self):
        print("SMS has been sent.")

emailnotification1=EmailNotification()
emailnotification1.send()

smsnotification1=SMSNotification()
smsnotification1.send()
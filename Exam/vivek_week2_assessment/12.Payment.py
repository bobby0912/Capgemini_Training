# •	12. Write a `Payment` class with a method `process_payment()`. 
# Implement subclasses `CreditCardPayment`, `PayPalPayment`, and 
# `BitcoinPayment` that override the method differently.
class Payment:
    def processPayment(self):
        print("welcome to payment section.")

class CreditCardPayment(Payment):
    def processPayment(self):
        print("Payment through credit card.")

class PayPalPayment(Payment):
    def processPayment(self):
        print("Payment through Paypal")

class BitcoinPayment(Payment):
    def processPayment(self):
        print("payment through bitcoin")


creditcard1=CreditCardPayment()
creditcard1.processPayment()


paypalpayment1=PayPalPayment()
paypalpayment1.processPayment()


bitcoinpayment1=BitcoinPayment()
bitcoinpayment1.processPayment()
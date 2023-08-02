#Liskov's substitution principle i.e it you objects in the program you should be able
# to replace those objects with instances of their subtypes or subclasses without 
# altering the correctness of the program


from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self,name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self,order,security_code):
        pass

class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("processing debit payment type")
        print("Verifying security code: %s"  %self.security_code)
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self,order):
        print("processing credit payment type")
        print("Verifying security code %s" %self.security_code)
        order.status = "paid"

class WalletPaymentProcessor(PaymentProcessor):

    def __init__(self, app_code):
        self.app_code = app_code

    def pay(self,order):
        print("processing wallet payment type")
        print("Verifying security code %s" %self.app_code)
        order.status = "paid"

order = Order()
order.add_item("Laptop",1,30000)
order.add_item('Mobile Phone', 1, 20000)
order.add_item('EarPhones', 2, 2000)

print(order.total_price())
payment_processor = WalletPaymentProcessor("333555")
payment_processor.pay(order)

#if walletpaymentprocessor wants app_code which is generated in mobile_app. So the other 
# two payment processors need security_code. So this value is passed through constructor
#now we are not voilating liskov's principle
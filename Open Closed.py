#Code should be open for extensibility and closed for modification
#We should be able to extend the existing code with new functionality
#We should not change the existing code for modification
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
    def pay(self, order, security_code):
        print("processing debit payment type")
        print("Verifying security code: %s"  %security_code)
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self,order, security_code):
        print("processing credit payment type")
        print("Verifying security code %s" %security_code)
        order.status = "paid"

class WalletPaymentProcessor(PaymentProcessor):
    def pay(self,order, security_code):
        print("processing wallet payment type")
        print("Verifying security code %s" %security_code)
        order.status = "paid"

order = Order()
order.add_item("Laptop",1,30000)
order.add_item('Mobile Phone', 1, 20000)
order.add_item('EarPhones', 2, 2000)

print(order.total_price())
payment_processor = WalletPaymentProcessor()
payment_processor.pay(order, "000077777")

#Here we have added another payment processor called wallet payment processor without modifying the 
# previos code 
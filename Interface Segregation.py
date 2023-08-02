#Interface Segregation i.e overall its better if you have several specific interfaces 
# instead of one general purpose interface


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



class SmsAuth():
    authorized = False
    def verify_code(self,code):
        print('Verifying code %s' %code)
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized

class DebitPaymentProcessorS(PaymentProcessor):

    def __init__(self, security_code, authorizer: SmsAuth):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized:
            raise Exception("Otp verification failed")
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

    def __init__(self, app_code, authorizer:SmsAuth):
        self.authorizer = authorizer
        self.app_code = app_code

    def pay(self,order):
        if not self.authorizer.is_authorized():
            raise Exception("Otp verification failed")
        print("processing wallet payment type")
        print("Verifying security code %s" %self.app_code)
        order.status = "paid"

order = Order()
order.add_item("Laptop",1,30000)
order.add_item('Mobile Phone', 1, 20000)
order.add_item('EarPhones', 2, 2000)

print(order.total_price())
smsauth = SmsAuth()
payment_processor = WalletPaymentProcessor("333555", smsauth)
smsauth.verify_code('123456')
payment_processor.pay(order)
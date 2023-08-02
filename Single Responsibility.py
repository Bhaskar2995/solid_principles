# Making classes and methods to have single responsibility

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
    
class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print("processing debit payment type")
        print("Verifying security code: %s"  %security_code)
        order.status = "paid"

    def pay_credit(self,order, security_code):
        print("processing credit payment type")
        print("Verifying security code %s" %security_code)
        order.status = "paid"

order = Order()
order.add_item("Laptop",1,30000)
order.add_item('Mobile Phone', 1, 20000)
order.add_item('EarPhones', 2, 2000)

print(order.total_price())
payment_processor = PaymentProcessor()
payment_processor.pay_debit(order, "000077777")


#Now order has single responsibility and paymentprocessor has single responsibility
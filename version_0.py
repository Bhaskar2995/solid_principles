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
    
    def pay(self,payment_type, security_code):
        if payment_type == "debit":
            print("processing debit payment type")
            print("Verifying security code: %s"  %security_code)
            self.status = "paid"
        elif payment_type == "credit":
            print("processing credit payment type")
            print("Verifying security code %s" %security_code)
        else:
            raise Exception("Unknown payment type %s" %payment_type)
        
order = Order()
order.add_item("Laptop",1,30000)
order.add_item('Mobile Phone', 1, 20000)
order.add_item('EarPhones', 2, 2000)

print(order.total_price())
order.pay("debit","000077777")
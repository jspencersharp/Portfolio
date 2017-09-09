from decimal import *

class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
        tax = .04


    def sold(self):
        self.status = "sold"
        return self

    def addTax(self, tax):
        Decimal(tax)
        self.price += tax
        return self

    def Return(self, reason):
        if reason == "Defective":
            self.status = "Defective"
            self.price = 0
            return self 

        # pass
    
    def show_all(self):
        print 'Price: ' + str(self.price)
        print 'Item Name: ' + str(self.item_name)
        print 'Weight: ' + str(self.weight)
        print 'Brand: ' + str(self.brand)
        print 'Cost: ' + str(self.cost)
        print 'Status: ' + str(self.status)
        return self

bottle1 = Product(19, "Bottle", 1, "simple", 5)
pen1 = Product(5, "Mr. Clicky Pen", 1, "Pilot", 1)

print "Greetings! How can I help you today?"
action = raw_input("Please choose from the following options: Buy, Check, Return")

# print action
# print isinstance(action, str)
if action == "Buy":
    bottle1.sold().show_all()
elif action == "Check":
    bottle1.addTax(.04).show_all()
elif action == "Return":
    reason = raw_input("Please type reason for return")
    bottle1.Return(reason)
    bottle1.show_all()
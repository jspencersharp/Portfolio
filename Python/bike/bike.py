class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "Price is $" + str(self.price)
        print "Max speed is: " + str(self.max_speed)
        print "Total miles: " + str(self.miles) + " miles"

    def ride(self):
        print "Driving..."
        self.miles =+ 10

    def reverse(self):
        print "Reversing..."
        self.miles =- 5



bike1 = Bike(300,100,22)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()


bike2 = Bike(22,4000,22)
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
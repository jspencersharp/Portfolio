class Car(object):
    def __init__(self, price, speed, fuel, milage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        self.tax = "12%"

    def taxRate(self):
        if self.price > 10000:
            self.tax = "15%"

    def displayAll(self):
        print"Price: ", self.price
        print"Speed: ", self.speed
        print"Fuel: ", self.fuel
        print"Milage: ", self.milage, "mpg"
        print"Tax: ", self.tax


car1 = Car(12000, 22, "reguar", 220)
car2 = Car(400, 18, "Electric", 200)
car3 = Car(500000, 200, "Jet Fuel", 12)
car4 = Car(9000, 54, "regular", 30000)
car5 = Car(250, 11, "push powered", 400)
car6 = Car(222, 22, "yes", 3112)

car1.taxRate()
car1.displayAll()
car2.taxRate()
car2.displayAll()
car3.taxRate()
car3.displayAll()
car4.taxRate()
car4.displayAll()
car5.taxRate()
car5.displayAll()
car6.taxRate()
car6.displayAll()
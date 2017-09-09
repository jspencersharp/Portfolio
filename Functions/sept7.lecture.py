# class that rep's superhero - name, city, powers, 


class Hero():
    def __init__ (self, name, city, powers):
        self.name = name
        self.city = city
        self.powers = powers

hero1 = Hero("superman", "New York", "x-ray vision")

print hero1.name


#create villain

class Villian():
    def __init__(self,name,city,powers):
        self.name=name
        self.city=city
        self.powers=powers

villian1=Villian("joker","gotham","violence")


class Sidekick():
    def __init__(self, name, city, powers):
        self.name=name
        self.city=city
        self.powers=powers

sidekick1 = Sidekick("bob","gotham","none")
class NFLTeam(object):
    def __init__ (self, name, color, city):
        self.name = name
        self.color = color
        self.city = city
        self.players = []
        
    
class Players(object):
    def __init__ (self, name, position, jersey_num):
        self.name = name
        self.position = position
        self.jersey_num = jersey_num

seahawks = NFLTeam("Seahawks", "Purple", "Seattle")
bob = Players("bob", "QB", 42)
seahawks.players.append(bob)

print seahawks.name
print seahawks.players[0].name

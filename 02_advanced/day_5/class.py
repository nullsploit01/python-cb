# Designing a game
# A player
# Attributes of player -> Name, health

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def __repr__(self):
        return f'Name: {self.name}, Health:{self.health}'
    
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} of damage, remaining health: {self.health}")

grom = Player("Grom", 100)
shelly = Player("Shelly", 100)

print(grom)
print(shelly)

grom.take_damage(25)
print(grom)
print(shelly)
from dinosaur import Dinosaur
class Robot:
    def __init__(self, name, power_level, health, Weapon):
        self.name = name
        self.power_level = power_level
        self.health = health
        self.weapon = Weapon
        self.attack_power = 2 * self.weapon.attack_power

    def attack(self, Dinosaur):
        print('The dinosaur attack!')


import random
from character import Character

class Monster(Character):
    def __init__(self):
        combat_strength = random.randint(1, 100)
        health_points = random.randint(1, 100)
        super().__init__(combat_strength, health_points)

    def monster_attacks(self):
        return random.randint(1, self.combat_strength)

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector.")
        super().__del__() 

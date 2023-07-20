import random
from src.loaders import player_name_generator


class Player:

    _name_generator = player_name_generator()

    def __init__(self, name, number, skills):
        self.name = name
        self.number = number
        self.skills = skills

    def __repr__(self):
        return f"<PLAYER: {self.name}>"

    @classmethod
    def random(cls):
        name = next(cls._name_generator)
        number = random.randint(1, 99)
        skills = {
            "reflex": random.randint(1, 20),
            "shoot": random.randint(1, 20)
        }
        return Player(name, number, skills)

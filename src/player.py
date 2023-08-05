import random
from src.loaders import player_name_generator


class Player:

    _name_generator = player_name_generator()

    def __init__(self, role, name, number, skills):
        self.role = role
        self.name = name
        self.number = number
        self.skills = skills

    def __repr__(self):
        return f"<PLAYER: {self.name}>"

    @classmethod
    def random(cls, number, role=None):
        assert role in (None, "GK", "DF", "MC", "FW"), "role is invalid"
        name = next(cls._name_generator)
        if role == "GK":
            skills = {
                "reflex": random.randint(10, 20),
                "shoot": random.randint(1, 10)
            }
        elif role == "DF":
            skills = {
                "reflex": random.randint(1, 5),
                "shoot": random.randint(5, 15)
            }
        elif role == "MC":
            skills = {
                "reflex": random.randint(1, 5),
                "shoot": random.randint(10, 20)
            }
        elif role == "FW":
            skills = {
                "reflex": random.randint(1, 5),
                "shoot": random.randint(15, 20)
            }
        else:
            skills = {
                "reflex": random.randint(1, 5),
                "shoot": random.randint(8, 20)
            }
        return Player(role, name, number, skills)

from src.player import Player
from src.loaders import team_name_generator


class Team:

    _name_generator = team_name_generator()

    def __init__(self, name):
        self.name = name
        self.players = []

    def __repr__(self):
        return "<TEAM: {}>".format(self.name.title())

    @classmethod
    def random(cls):
        name = next(cls._name_generator)
        t = Team(name)
        for _ in range(11):
            t.players.append(Player.random())
        return t

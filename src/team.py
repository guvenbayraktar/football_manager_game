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
        t.players.append(Player.random(number=1, role="GK"))
        for i in range(4):
            t.players.append(Player.random(number=i+2, role="DF"))
        for i in range(4):
            t.players.append(Player.random(number=i+6, role="MC"))
        for i in range(2):
            t.players.append(Player.random(number=i+10, role="FW"))
        return t

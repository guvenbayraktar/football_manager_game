from src.player import Player
from src.team import Team

p = Player.random()

print(p)

t = Team.random()

print(t)
# print(t.players)

for index, player in enumerate(t.players, start=1):
    print(index, player)

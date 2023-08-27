from src.team import Team

t = Team.random()

print(t)
# print(t.players)

for index, player in enumerate(t.players, start=1):
    print(player.role, player.number, player.name, player.skills)

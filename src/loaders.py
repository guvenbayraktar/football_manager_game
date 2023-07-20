import random


def team_name_generator():
    with open("resources/country.txt") as f:
        data = f.read().split("\n")
    random.shuffle(data)
    for name in data:
        yield name


def player_name_generator():
    with open("resources/names.txt") as f:
        data = f.read().split("\n")[:-1]
    while True:
        yield random.choice(data)

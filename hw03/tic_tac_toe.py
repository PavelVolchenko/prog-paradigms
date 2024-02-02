from itertools import cycle


def print_field():
    for i in range(1, 10):
        if i % 3 == 0:
            print(f'{field[i - 1]}\n', end='')
        else:
            print(f'{field[i - 1]}|', end='')


def turn(player, position):
    if (
            field[position] == zero or
            field[position] == cross
    ):
        print("Эта клетка занята. Выберите другую:")
        next(players)
    else:
        field[position] = player
    print_field()
    return winner_check(field, player)


def winner_check(field, player):
    winning_combination = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 4, 8),
        (2, 4, 6),
        (0, 3, 6),
        (2, 5, 8),
        (1, 4, 7),
    )
    for i in winning_combination:
        if (
                field[i[0]] == player and
                field[i[1]] == player and
                field[i[2]] == player
        ):
            print("Победа", player)
            return True
    return False


print("Крестики-нолики")
field = [chr(9312 + i) for i in range(9)]
print_field()
players = cycle([
    cross := chr(128939),
    zero := chr(128901)],
)

winner = False
while not winner:
    player = next(players)
    try:
        position = int(input(f"Ход {player}\n")) - 1
        winner = turn(player, position)
    except:
        print("Введите от 1 до 9:\n")
        player = next(players)

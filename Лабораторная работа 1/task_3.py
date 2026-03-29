players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

one_players = players[::2]
two_players = players[::-2]

quantity_players = len(players) // 2

one_players = players[:quantity_players]
two_players = players[quantity_players:]

print(one_players)
print(two_players)

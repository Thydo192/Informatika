list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
# найдем середину
F = len(list_players) // 2
# раздели команду на две равные
team_A = list_players[:F]
team_B = list_players[F:]
# выведем список учатсников каждой команды
print(team_A)
print(team_B)

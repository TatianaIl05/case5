from prettytable import PrettyTable
import STARVE
import METEOR_RAIN

food = [10000, 10000, 10000, 10000]
people = [7000, 7000, 7000, 7000]
attack = [100, 100, 100, 100]
usage = [people[0] * 0.5, people[1]*0.5, people[2]*0.5, people[3]*0.5]
defense = [5000, 5000, 5000, 5000]


def start_info():
    print(f'\n Ход {step + 1} команды {team + 1}')
    food[team], people[team], usage[team] = STARVE.starve(food[team], people[team], usage[team])
    print('Данные на начало хода: ')
    table_columns = ['Люди', 'Еда', 'Защита', 'Атака', 'Потребление']
    table = PrettyTable(table_columns)
    table.add_row([people[team], food[team], defense[team], attack[team], usage[team]])
    print(table)


for step in range(7):
    for team in range(4):
        start_info()
        people[team], defense[team] = METEOR_RAIN.meteor_rain(defense[team], food[team])



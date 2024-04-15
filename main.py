from prettytable import PrettyTable
import STARVE

food = [10000, 10000, 10000, 10000]
people = [7000, 7000, 7000, 7000]
attack = [100, 100, 100, 100]
# usage = [people[0] * 0.5, people[1]*0.5, people[2]*0.5, people[3]*0.5]
usage = [3500, 3500, 3500, 3500]
defense = [50, 50, 50, 50]


def start_info():
    print(f'\n Ход {step + 1} команды {team + 1}')
    food[team], people[team], usage[team] = STARVE.starve(food[team], people[team], usage[team])
    print('Данные на начало хода: ')
    table_columns = ['Люди', 'Еда', 'Защита', 'Атака', 'Потребление']
    table = PrettyTable(table_columns)
    table.add_row([people[team], food[team], defense[team], attack[team], usage[team]])
    print(table)


for step in range(4):
    for team in range(1):
        start_info()



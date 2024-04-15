from prettytable import PrettyTable
import STARVE
import METEOR_RAIN
import CHECK
import case

food = [10000, 10000, 10000, 10000]
people = [7000, 7000, 7000, 7000]
ar = [1, 1, 1, 1]
attack = [int(people[0] * 0.3) * ar[0], int(people[1] * 0.3) * ar[1], int(people[2] * 0.3) * ar[2],
          int(people[3] * 0.3) * ar[3]]
usage = [people[0] * 0.5, people[1] * 0.5, people[2] * 0.5, people[3] * 0.5]
defense = [5000, 5000, 5000, 5000]


def start_info():
    food[team], people[team], usage[team] = STARVE.starve(food[team], people[team], usage[team])
    print('Данные на начало хода: ')
    table_columns = ['Люди', 'Еда', 'Защита', 'Атака', 'Потребление']
    table = PrettyTable(table_columns)
    table.add_row([people[team], food[team], defense[team], attack[team], usage[team]])
    print(table)


for step in range(7):
    for team in range(1):
        print(f'\n Ход {step + 1} команды {team + 1}')
        people[team], defense[team] = METEOR_RAIN.meteor_rain(people[team], defense[team])
        start_info()
        people[team], ar[team], defense[team], flag = case.case(people[team], ar[team], attack[team],
                                                                defense[team], flag=None)
        attack[team] = int(people[team] * 0.3 * ar[team])
        if flag == 'red':
            print('Кому хотите объявить войну?')
        # CHECK.check_war()

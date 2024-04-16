from prettytable import PrettyTable
from random import randint
import STARVE
import METEOR_RAIN
import CHECK
import case
import random_events as ran
import ru_local as ru

food = [10000, 10000, 10000, 10000]
people = [7000, 7000, 7000, 7000]
ar = [1, 1, 1, 1]
attack = [int(people[0] * 0.3) * ar[0], int(people[1] * 0.3) * ar[1], int(people[2] * 0.3) * ar[2],
          int(people[3] * 0.3) * ar[3]]
usage = [people[0] * 0.5, people[1] * 0.5, people[2] * 0.5, people[3] * 0.5]
defense = [5000, 5000, 5000, 5000]
findings = [0, 0, 0, 0]
research_tools = [20, 20, 20, 20]


def start_info():
    food[team - 1], people[team - 1], usage[team - 1] = STARVE.starve(food[team - 1], people[team - 1], usage[team - 1])
    print('Данные на начало хода: ')
    table_columns = ['Люди', 'Еда', 'Защита', 'Атака', 'Потребление', 'Артефакты']
    table = PrettyTable(table_columns)
    table.add_row([people[team], food[team], defense[team], attack[team], usage[team], findings[team]])
    print(table)


rival_teams = [0] * 12


def question():
    global team, step
    if input(ru.DESIRE_CHALLENGE).lower() == ru.YES_NO:
        compete_team = int(input(ru.NUM_TEAM))
        while compete_team == team or compete_team > 4:
            print(ru.VALUE_ERROR)
            compete_team = int(input(ru.OTHER_VALUE))
        rival_teams[team - 1 + 4 * step] = compete_team
        print(ru.TEAM, team, ru.CHALLENGED, compete_team)


def answer():
    global team, step
    for k in range(len(rival_teams)):
        if rival_teams[k] == team:
            if input(f'{ru.APPROVAL_TEAM} {team} {ru.BATTLE} '
                     f'{int((k + 1) % 4) if (k + 1) % 4 != 0 else 4}? ').lower() == ru.YES_NO:
                print(ru.FIGHT)
                battle()
            else:
                print(ru.NOT_FIGHT)
                reconcile()


def battle():
    global step
    num_ask = randint(1, 100)
    num_accept = randint(1, 100)
    print(ru.TEAM_CHELLENGE, num_ask, ru.SECOND_TEAM, num_accept)
    if num_ask > num_accept:
        food[rival_teams.index(team) - 4 * step] += 0.5 * food[team - 1]
        food[team - 1] *= 0.5
    elif num_ask < num_accept:
        food[team - 1] += 0.5 * food[rival_teams.index(team) - 4 * step]
        food[rival_teams.index(team) - 4 * step] *= 0.5
    else:
        food[team - 1] += 50
        food[rival_teams.index(team) - 4 * step] += 50
    print(ru.RESOURCES_EQUAL, food[rival_teams.index(team) - 4 * step], food[team - 1])
    rival_teams[rival_teams.index(team)] = 0


def reconcile():
    global step
    food[team - 1] *= 0.8
    people[rival_teams.index(team) - 4 * step] *= 0.8
    print(ru.RESOURCES_EQUAL, people[rival_teams.index(team) - 4 * step], food[team - 1])
    rival_teams[rival_teams.index(team)] = 0


for step in range(4):
    for team in range(1, 4 + 1):
        print(f'\n Ход {step + 1} команды {team}')
        people[team - 1], defense[team - 1] = METEOR_RAIN.meteor_rain(people[team - 1], defense[team - 1])
        start_info()
        ran.sickness(people[team - 1])
        ran.artifacts(findings[team - 1])
        people[team - 1], ar[team - 1], defense[team - 1], flag = case.case(people[team - 1], ar[team - 1],
                                                                            attack[team - 1], defense[team - 1],
                                                                            flag=None)
        if flag == 'red':
            ran.artifacts(findings[team - 1])
        attack[team - 1] = int(people[team - 1] * 0.3 * ar[team - 1])
        answer()
        question()

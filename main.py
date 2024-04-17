from prettytable import PrettyTable
from random import randint
import STARVE
import METEOR_RAIN
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
rival_teams = [0] * 12


def start_info():
    '''
    This function outputs the initial data of the round.
    :return: None
    '''
    food[team - 1], people[team - 1], usage[team - 1] = STARVE.starve(food[team - 1], people[team - 1], usage[team - 1])
    print(ru.START_DATA)
    table_columns = [ru.PEOPLES_TABLE, ru.FOOD, ru.DEFENSES, ru.ATTACK, ru.CONSUMPTION, ru.FINDINGS]
    table = PrettyTable(table_columns)
    table.add_row(
        [people[team - 1], food[team - 1], defense[team - 1], attack[team - 1], usage[team - 1], findings[team - 1]])
    print(table)


def alien_invasion(team_num):
    probability = randint(1, 100) / 100

    if probability > 0.8:
        print(ru.ALIEN_ATTACK)
        people[team_num - 1] *= 0.9
        defense[team_num - 1] *= 0.9
        print(ru.CREW, people[team_num - 1], ru.DEFENSE, defense[team_num - 1])


def question():
    '''
    This function offers a command to challenge another team to a duel.
    :return: None
    '''
    global team, step
    if input(ru.DESIRE_CHALLENGE).lower() == ru.YES_NO:
        compete_team = int(input(ru.NUM_TEAM))
        while compete_team == team or compete_team > 4:
            print(ru.VALUE_ERROR)
            compete_team = int(input(ru.OTHER_VALUE))
        rival_teams[team - 1 + 4 * step] = compete_team
        print(ru.TEAM, team, ru.CHALLENGED, compete_team)


def answer():
    '''
    This feature prompts a team to accept a challenge to a fight from another team.
    :return: None
    '''
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
    '''
    This function determines the result of the match between the teams.
    :return: None
    '''
    if attack[team - 1] == attack[rival_teams.index(team) - 4 * step]:
        food[team - 1] += 50
        food[rival_teams.index(team) - 4 * step] += 50
        print(ru.DRAW)
    elif attack[team - 1] > attack[rival_teams.index(team) - 4 * step]:
        food[team - 1] += 0.5 * food[rival_teams.index(team) - 4 * step]
        food[rival_teams.index(team) - 4 * step] *= 0.5
        findings[team - 1] += findings[rival_teams.index(team) - 4 * step]
        findings[rival_teams.index(team) - 4 * step] = 0
        team_win = team
        print(ru.TWO_FIGHT_WINNER, food[team_win - 1], findings[team_win - 1])
    else:
        food[rival_teams.index(team) - 4 * step] += 0.5 * food[team - 1]
        food[team - 1] *= 0.5
        findings[rival_teams.index(team) - 4 * step] += findings[team - 1]
        findings[team - 1] = 0
        team_win = rival_teams.index(team) - 4 * step + 1
        print(ru.TWO_FIGHT_WINNER, food[team_win - 1], findings[team_win - 1])
    print(ru.RESOURCES_EQUAL, ru.FOODS, food[rival_teams.index(team) - 4 * step], food[team - 1],
          ru.ARTEFACTS, findings[rival_teams.index(team) - 4 * step],  findings[team - 1])
    rival_teams[rival_teams.index(team)] = 0


def reconcile():
    '''
    This function determines the result of the truce of the teams.
    :return: None
    '''
    global step
    food[team - 1] *= 0.8
    people[rival_teams.index(team) - 4 * step] *= 0.8
    print(ru.RESOURCES_EQUAL, ru.COMMENT, people[rival_teams.index(team) - 4 * step], food[team - 1])
    rival_teams[rival_teams.index(team)] = 0


for step in range(3):
    for team in range(1, 4 + 1):
        print(f'\n {ru.MOTION} {step + 1} {ru.TEAM_NUMBER} {team}')
        start_info()
        people[team - 1], defense[team - 1] = METEOR_RAIN.meteor_rain(people[team - 1], defense[team - 1])
        ran.sickness(people[team - 1])
        alien_invasion(team)
        people[team - 1], ar[team - 1], defense[team - 1], food[team - 1], flag = case.case(people[team - 1],
                                                                                            ar[team - 1],
                                                                                            attack[team - 1],
                                                                                            defense[team - 1],
                                                                                            food[team - 1],
                                                                                            flag=None)
        if flag == ru.RED:
            findings[team - 1] = ran.artifacts(findings[team - 1])
        attack[team - 1] = int(people[team - 1] * 0.3 * ar[team - 1])
        answer()
        question()

sum_ = [0, 0, 0, 0]
for team in range(1, 4 + 1):
    sum_[team - 1] = food[team - 1] + people[team - 1] + defense[team - 1] + (findings[team - 1] * 2000)
print(f'{ru.WIN_TEAM} {sum_.index(max(sum_)) + 1} {ru.ACCOUNT} {max(sum_)}')

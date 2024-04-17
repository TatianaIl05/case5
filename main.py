from prettytable import PrettyTable
import random
import ru_local as ru

food = [10000, 10000, 10000, 10000]
people = [7000, 7000, 7000, 7000]
ar = [1, 1, 1, 1]
attack = [int(people[0] * 0.3) * ar[0], int(people[1] * 0.3) * ar[1], int(people[2] * 0.3) * ar[2],
          int(people[3] * 0.3) * ar[3]]
usage = [people[0] * 0.5, people[1] * 0.5, people[2] * 0.5, people[3] * 0.5]
defense = [5000, 5000, 5000, 5000]
findings = [0, 0, 0, 0]
rival_teams = {1: 0, 2: 0, 3: 0, 4: 0}
rivals = []


def starve(food, people, usage):
    '''
    This function declares hunger when the food value of the team is low.
    :param food: food count
    :param people: number of people in team
    :param usage: usage
    :return: [food - usage, people, people * 0.5]
    '''
    if usage > food:
        print(f'{ru.HUNGER} {int(abs(food - usage))} {ru.PEOPLES}')
        return [0, people - abs(food - usage), (people - abs(food - usage)) * 0.5]
    else:
        return [food - usage, people, people * 0.5]


def start_info():
    '''
    This function outputs the initial data of the round.
    :return: None
    '''
    food[team - 1], people[team - 1], usage[team - 1] = starve(food[team - 1], people[team - 1], usage[team - 1])
    print(ru.START_DATA)
    table_columns = [ru.PEOPLES_TABLE, ru.FOOD, ru.DEFENSES, ru.ATTACK, ru.CONSUMPTION, ru.FINDINGS]
    table = PrettyTable(table_columns)
    table.add_row(
        [people[team - 1], food[team - 1], defense[team - 1], attack[team - 1], usage[team - 1], findings[team - 1]])
    print(table)


def meteor_rain(people, defense):
    '''
    This function triggers a random event in the form of a meteorite impact.
    :param people: number of people in team
    :param defense: defense count
    :return: people, defense
    '''
    meteor_chance = random.randint(1, 3)
    if meteor_chance == 1:
        if defense < 2000:
            print(f'{ru.METEORITE} {people - int(people * 0.7)} {ru.PEOPLES}')
            return [int(people * 0.7), 0]
        else:
            print(f'{ru.METEORITE} {defense * 0.5} {ru.DEFENSES2}')
            return [people, defense * 0.5]
    else:
        return [people, defense]


def case(people, ar, attack, defense, food, flag=None):
    '''
    This function offers the team a choice of action
    in its turn. From a random event to non-random ones.
    :param people: people count
    :param ar: ar
    :param attack: attack count
    :param defense: defense count
    :param food: food count
    :param flag: flag
    :return: None
    '''
    print(f'{ru.CHOOSING_ACTION} \n {ru.CHOICE_ATTACK} \n {ru.CHOICE_DEFENSE} \n {ru.CHOICE_LOCATION} '
          f'\n {ru.CHOICE_FOOD}')
    var = int(input())
    match var:
        case 1:
            ar += 0.3
            print(f'{ru.UPGRADE_ATTACK} {attack * ar}')
            return [people, ar, attack, defense, food, flag]
        case 2:
            defense += 200
            print(f'{ru.UPGRADE_DEFENSE} {defense}')
            return [people, ar, attack, defense, food, flag]
        case 3:
            flag = ru.RED
            return [people, ar, attack, defense, food, flag]
        case 4:
            print(f'{ru.UPGRADE_FOOD} {food + 6000} {ru.FOOD1}')
            return [people, ar, attack, defense, food + 6000, flag]
        case _:
            print(ru.MISTAKE)
            return case(people, ar, attack, defense, food, flag=None)


def sickness(people):
    '''
    This function determines if the team gets sick.
    :param people: number of people in team
    :return: None
    '''
    roulette_death = (200, 30, 80, 120, 5, 300)
    result_death = random.choice(roulette_death)
    roulette_failure = (1, 2)
    result_failure = random.choice(roulette_failure)
    if result_failure == 1:
        print(ru.DISEASE)
        people -= result_death
        print(f'{ru.LOST} {people} {ru.PEOPLES}')


def artifacts(findings):
    '''
    This function determines whether the team finds a valuable artifact.
    :param findings: number of valuable artefacts
    :return: None
    '''
    items = (1, 2, 4, 3, 6, 8, 9)
    result_items = random.choice(items)
    if result_items % 2 == 0:
        print(ru.ARTEFACT)
        findings += 1
    elif result_items == 3:
        print(ru.ARTEFACT3)
        findings += 3
    else:
        print(ru.SEARCH_RESULT)
    return findings


def alien_invasion(team_num):
    probability = random.randint(1, 100) / 100

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
    global team
    if input(ru.DESIRE_CHALLENGE).lower() == ru.YES_NO:
        compete_team = int(input(ru.NUM_TEAM))
        while compete_team == team or compete_team > 4:
            print(ru.VALUE_ERROR)
            compete_team = int(input(ru.OTHER_VALUE))
        rival_teams[team] = compete_team
        print(ru.TEAM, team, ru.CHALLENGED, compete_team)


def answer():
    '''
    This feature prompts a team to accept a challenge to a fight from another team.
    :return: None
    '''
    global team
    for k in range(1, 4 + 1):
        if rival_teams[k] == team:
            rivals.append(k)
            if input(f'{ru.APPROVAL_TEAM} {team} {ru.BATTLE} '
                     f'{k % 4 if k % 4 != 0 else 4}? ').lower() == ru.YES_NO:
                print(ru.FIGHT)
                battle()
            else:
                print(ru.NOT_FIGHT)
                reconcile()
            rivals.pop(0)
            rival_teams[k] = 0


def battle():
    '''
    This function determines the result of the match between the teams.
    :return: None
    '''
    if int(attack[team - 1]) == int(attack[rivals[0] - 1]):
        food[team - 1] += 50
        food[rivals[0] - 1] += 50
        print(ru.DRAW)
    elif attack[team - 1] > attack[rivals[0] - 1]:
        food[team - 1] += 0.5 * food[rivals[0] - 1]
        food[rivals[0] - 1] *= 0.5
        findings[team - 1] += findings[rivals[0] - 1]
        findings[rivals[0] - 1] = 0
        team_win = team
        print(ru.TWO_FIGHT_WINNER, team_win, ru.RES_COM, food[team_win - 1], findings[team_win - 1])
    else:
        food[rivals[0] - 1] += 0.5 * food[team - 1]
        food[team - 1] *= 0.5
        findings[rivals[0] - 1] += findings[team - 1]
        findings[team - 1] = 0
        team_win = rivals[0]
        print(ru.TWO_FIGHT_WINNER, team_win, ru.RES_COM, food[team_win - 1], findings[team_win - 1])
    print(ru.RESOURCES_EQUAL, ru.FOODS, food[rivals[0] - 1], food[team - 1],
          ru.ARTEFACTS, findings[rivals[0] - 1],  findings[team - 1])


def reconcile():
    '''
    This function determines the result of the truce of the teams.
    :return: None
    '''
    global step
    food[team - 1] *= 0.8
    people[rivals[0] - 1] *= 0.8
    print(ru.RESOURCES_EQUAL, ru.COMMENT, people[rivals[0] - 1], food[team - 1])


for step in range(3):
    for team in range(1, 4 + 1):
        print(f'\n {ru.MOTION} {step + 1} {ru.TEAM_NUMBER} {team}')
        start_info()
        people[team - 1], defense[team - 1] = meteor_rain(people[team - 1], defense[team - 1])
        sickness(people[team - 1])
        alien_invasion(team)
        people[team - 1], ar[team - 1], attack[team - 1], defense[team - 1], food[team - 1], flag = (
            case(people[team - 1], ar[team - 1], attack[team - 1], defense[team - 1], food[team - 1], flag=None))
        if flag == ru.RED:
            findings[team - 1] = artifacts(findings[team - 1])
        attack[team - 1] = int(people[team - 1] * 0.3 * ar[team - 1])
        answer()
        question()

sum_ = [0, 0, 0, 0]
for team in range(1, 4 + 1):
    sum_[team - 1] = food[team - 1] + people[team - 1] + defense[team - 1] + (findings[team - 1] * 2000)
print(f'{ru.WIN_TEAM} {sum_.index(max(sum_)) + 1} {ru.ACCOUNT} {max(sum_)}')

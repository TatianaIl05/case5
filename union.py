class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.velocity = 20
        self.trace_points = []

team_1 = Player(input('Введите имя команды 1: '), 50, 50)
team_2 = Player(input('Введите имя команды 2: '), 550, 550)
team_3 = Player(input('Введите имя команды 3: '), 50, 550)
team_4 = Player(input('Введите имя команды 4: '), 550, 50)

players = [team_1, team_2, team_3, team_4]
current_team = 1

rival_teams = [0, 0, 0, 0]
food = [2000, 2000, 2000, 2000]
people = [7000, 7000, 7000, 7000]
#-----------------------------------------------------------------------То что сверху уже есть в коде

'''def union():
    food[rival_teams[current_team - 1] - 1] = (food[current_team - 1] + food[rival_teams[current_team - 1] - 1]) // 2
    food[current_team - 1] = (food[current_team - 1] + food[rival_teams[current_team - 1] - 1]) // 2
def refusal_union():
    people[current_team - 1] -= 400'''

def question_union():
    global current_team
    if input('У Вас есть возможность взаимодействовать с другими командами. '
             'Хотите ли Вы предложить кому-то союз? ').lower() == 'да':
        compete_team = int(input('Введите номер команды для предложения союза: '))
        while compete_team == current_team or compete_team > 4:
            print('Неверное значение')
            compete_team = int(input('Введите другое значение: '))
        rival_teams[compete_team - 1] = current_team
        print(f'Команда {current_team} предложила союз {compete_team}')

question_union()

def answer_union():
    global current_team
    if rival_teams[current_team - 1] != 0:
        if input(f'Согласна ли команда {current_team} на союз с'
                 f' командой {rival_teams[current_team - 1]}? ').lower() == 'да':
            print('Дружба - это сила')
            food[rival_teams[current_team - 1] - 1] = (food[current_team - 1] + food[
                rival_teams[current_team - 1] - 1]) // 2
            food[current_team - 1] = (food[current_team - 1] + food[rival_teams[current_team - 1] - 1]) // 2
            # return ['f', food[current_team - 1]]
        else:
            print('Отказ от союза')
            people[current_team - 1] -= 400
            # return ['w', people[current_team - 1]]
answer_union()

def battle1():
    global step, compete_team
    print(attack[team-1])
    print(defense[compete_team - 1])
    if attack[compete_team - 1] > defense[rival_teams.index(team) - 4*step]:
        food[rival_teams.index(team) - 4*step] += 0.5 * food[team - 1]
        food[team - 1] *= 0.5
        print(f'Команда {compete_team} выиграла!')
    elif attack[rival_teams.index(team) - 1] > defense[compete_team - 1]:
        food[team - 1] += 0.5 * food[rival_teams.index(team) - 4*step]
        food[rival_teams.index(team) - 4*step] *= 0.5
        print(f'Команда {rival_teams[team]} выиграла!')
    elif attack[compete_team - 1] == defense[rival_teams.index(team) - 4*step] and attack[rival_teams.index(team) - 1] == defense[compete_team - 1]:
        food[team - 1] += 50
        food[rival_teams.index(team) - 4*step] += 50
    print(ru.RESOURCES_EQUAL, food[rival_teams.index(team) - 4*step], food[team - 1])
    rival_teams[rival_teams.index(team)] = 0


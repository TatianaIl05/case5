import pygame
from random import randint
from prettytable import PrettyTable

food = [14000, 14000, 14000, 14000]
people = [7000, 7000, 7000, 7000]
findings = [0, 0, 0, 0]
research_tools = [20, 20, 20, 20]
defense = [50, 50, 50, 50]

pygame.init()
screen = pygame.display.set_mode((600, 600))
background = pygame.image.load('space_background.png')


class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.velocity = 20
        self.trace_points = []

    def move(self):
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_LEFT:
                    self.x -= self.velocity
                case pygame.K_RIGHT:
                    self.x += self.velocity
                case pygame.K_UP:
                    self.y -= self.velocity
                case pygame.K_DOWN:
                    self.y += self.velocity

            screen_width, screen_height = 600, 600
            self.x = max(0, min(self.x, screen_width - 10))
            self.y = max(0, min(self.y, screen_height - 10))
            self.trace_points.append((self.x+5, self.y+5))

    def draw(self, color1):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, color1, (self.x, self.y, 10, 10))

    def trace(self, color2):
        for point in self.trace_points:
            pygame.draw.rect(screen, color2, (point[0], point[1], 1, 1))

    def do(self, color1, color2):
        self.move()
        self.draw(color1)
        self.trace(color2)


class HealthBar:
    def __init__(self, x, y, max_hp, width, colour):
        self.x = x
        self.y = y
        self.width = width
        self.hp = max_hp
        self.max_hp = max_hp
        self.colour = colour

    def draw(self):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, 'black', (self.x, self.y, self.max_hp, self.width))
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.max_hp * ratio, self.width))


team_1 = Player(input('Введите имя команды 1: '), 50, 50)
team_2 = Player(input('Введите имя команды 2: '), 550, 550)
team_3 = Player(input('Введите имя команды 3: '), 50, 550)
team_4 = Player(input('Введите имя команды 4: '), 550, 50)

bar_1 = HealthBar(10, 10, people[0]/100, 20, 'red')
bar_2 = HealthBar(520, 570, people[1]/100, 20, 'yellow')
bar_3 = HealthBar(10, 570, people[2]/100, 20, 'green')
bar_4 = HealthBar(520, 10, people[3]/100, 20, 'blue')

players = [team_1, team_2, team_3, team_4]
square_colors = ['red', 'yellow', 'green', 'blue']
trace_colors = ['pink', 'white', 'light green', 'light blue']


def alien_invasion(team):
    probability = randint(1, 100)/100
    if 220 < team.x < 320 and 380 < team.y < 480:
        probability = 1
    if probability > 0.9:
        print('Нападение инопланетных рас')
        people[players.index(team)] *= 0.9
        defense[players.index(team)] *= 0.9
        print(f'Экипаж: {people[players.index(team)]}, Средства защиты: {defense[players.index(team)]}')


def monthly_food(team):
    food[players.index(team)] += 1000
    food[players.index(team)] -= people[players.index(team)]//4
    return food[players.index(team)]


rival_teams = [0] * 12


def question():
    global current_team, j
    if input('Хотите ли Вы бросить кому-то вызов? ').lower() == 'да':
        compete_team = int(input('Введите номер команды, с которой вы будете соревноваться: '))
        while compete_team == current_team or compete_team > 4:
            print('Неверное значение')
            compete_team = int(input('Введите другое значение: '))
        rival_teams[current_team - 1 + 4*j] = compete_team
        print(f'Команда {current_team} бросила вызов команде {compete_team}')


def answer():
    global current_team, j
    for k in range(len(rival_teams)):
        if rival_teams[k] == current_team:
            if input(f'Согласна ли команда {current_team} на противостояние с'
                     f' командой {int((k+1) % 4) if (k+1) % 4 != 0 else int((k+5)/(j+1))}? ').lower() == 'да':
                print('Противостояние')
                battle()
            else:
                print('Отказ от противостояния')
                reconcile()


def battle():
    global j
    num_ask = randint(1, 100)
    num_accept = randint(1, 100)
    print(f'Команда, бросившая вызов: {num_ask}, Вторая команда: {num_accept}')
    if num_ask > num_accept:
        food[rival_teams.index(current_team) - 4*j] += 0.5*food[current_team - 1]
        food[current_team - 1] *= 0.5
    elif num_ask < num_accept:
        food[current_team - 1] += 0.5 * food[rival_teams.index(current_team) - 4*j]
        food[rival_teams.index(current_team) - 4*j] *= 0.5
    else:
        food[current_team - 1] += 50
        food[rival_teams.index(current_team) - 4*j] += 50
    print(f'Ресурсы команд равны: {food[rival_teams.index(current_team) - 4*j]} и {food[current_team - 1]}')
    rival_teams[rival_teams.index(current_team)] = 0


def reconcile():
    global j
    food[current_team - 1] *= 0.8
    people[rival_teams.index(current_team) - 4*j] *= 0.8
    print(f'Ресурсы команд равны: {people[rival_teams.index(current_team) - 4*j]} и {food[current_team - 1]}')
    rival_teams[rival_teams.index(current_team)] = 0


running = True
current_team = 1
count_times = 0
j = 0

while running:
    bar_1.draw()
    bar_2.draw()
    bar_3.draw()
    bar_4.draw()
    if j > 2:
        running = False
        print('Игра окончена!!!')
    if 0 in people:
        people[people.index(0)] = 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                if current_team == 1 or current_team == 2 or current_team == 3 or current_team == 4:
                    current_team += 1
                if current_team == 5:
                    current_team = 1
        match current_team:
            case 1:
                team_1.do(square_colors[0], trace_colors[0])
                if count_times == 0:
                    print('Ход первой команды')
                    print('За этот месяц во время путешествия произошло несколько событий: ')
                    print(f'Изменение ресурса - пропитание {monthly_food(team_1)}')
                    alien_invasion(team_1)
                    print('Взаимодействия команд: ')
                    answer()
                    question()
                    bar_1.hp = people[0]/100
                    count_times += 1
            case 2:
                team_2.do(square_colors[1], trace_colors[1])
                if count_times == 1:
                    print('Ход второй команды')
                    print('За этот месяц во время путешествия произошло несколько событий: ')
                    alien_invasion(team_2)
                    print(f'Изменение ресурса - пропитание {monthly_food(team_2)}')
                    print('Взаимодействия команд: ')
                    answer()
                    question()
                    bar_2.hp = people[1] / 100
                    count_times += 1
            case 3:
                team_3.do(square_colors[2], trace_colors[2])
                if count_times == 2:
                    print('Ход третьей команды')
                    print('За этот месяц во время путешествия произошло несколько событий: ')
                    print(f'Изменение ресурса - пропитание {monthly_food(team_3)}')
                    alien_invasion(team_3)
                    print('Взаимодействия команд: ')
                    answer()
                    question()
                    bar_3.hp = people[2] / 100
                    count_times += 1
            case 4:
                team_4.do(square_colors[3], trace_colors[3])
                if count_times == 3:
                    print('Ход четвёртой команды')
                    print('За этот месяц во время путешествия произошло несколько событий: ')
                    print(f'Изменение ресурса - пропитание {monthly_food(team_4)}')
                    alien_invasion(team_4)
                    print('Взаимодействия команд: ')
                    answer()
                    question()
                    bar_4.hp = people[3] / 100
                    count_times = 0
                    resource_table = PrettyTable()
                    resource_table.add_column('Команды', [1, 2, 3, 4])
                    resource_table.add_column('Пропитание', food)
                    resource_table.add_column('Экипаж', people)
                    resource_table.add_column('Ценные находки', findings)
                    resource_table.add_column('Средства защиты', defense)
                    resource_table.add_column('Средства изучения', research_tools)
                    print(resource_table)
                    j += 1

        for i in range(1, 4 + 1):
            if i != current_team:
                pygame.draw.rect(screen, square_colors[i - 1], pygame.Rect(players[i - 1].x, players[i - 1].y, 10, 10))
                for point in players[i - 1].trace_points:
                    pygame.draw.rect(screen, trace_colors[i - 1], pygame.Rect(point[0], point[1], 1, 1))
    pygame.display.update()

pygame.quit()

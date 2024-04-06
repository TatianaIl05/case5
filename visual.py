import pygame
from random import randint
from prettytable import PrettyTable

food = [2000, 2000, 2000, 2000]
people = [1000, 1000, 1000, 1000]
findings = [0, 0, 0, 0]
research_tools = [20, 20, 20, 20]
protection_means = [50, 50, 50, 50]

pygame.init()


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
        pygame.draw.rect(screen, color1, pygame.Rect(self.x, self.y, 10, 10))

    def trace(self, color2):
        for point in self.trace_points:
            pygame.draw.rect(screen, color2, pygame.Rect(point[0], point[1], 1, 1))

    def do(self, color1, color2):
        self.move()
        self.draw(color1)
        self.trace(color2)


team_1 = Player(input('Введите имя команды 1: '), 50, 50)
team_2 = Player(input('Введите имя команды 2: '), 550, 550)
team_3 = Player(input('Введите имя команды 3: '), 50, 550)
team_4 = Player(input('Введите имя команды 4: '), 550, 50)

players = [team_1, team_2, team_3, team_4]
square_colors = ['red', 'yellow', 'green', 'blue']
trace_colors = ['pink', 'white', 'light green', 'light blue']

screen = pygame.display.set_mode((600, 600))
background = pygame.image.load('space_background.png')

running = True
current_team = 1


def alien_invasion(team):
    probability = randint(1, 100)/100

    if probability > 0.9:
        print('Нападение инопланетных рас')
        people[players.index(team)] *= 0.9
        protection_means[players.index(team)] *= 0.9
        print(team.x, team.y)
        print(people[players.index(team)], protection_means[players.index(team)])


def monthly_food(team):
    food[players.index(team)] += 1000
    food[players.index(team)] -= people[players.index(team)]//4
    print(food[players.index(team)])


def question(team):
    if current_team == team:
        if input('У Вас есть возможность взаимодействовать с другими командами. '
                 'Хотите ли Вы бросить кому-то вызов?').lower() == 'да':
            compete_team = input('Введите название команды, с которой вы будете соревноваться: ')
            print(f'Команда {team} бросила вызов команде {compete_team}')


@ question
def answer(team):
    if current_team == team:
        if input(f'Согласна ли команда на противостояние?').lower() == 'да':
            print('Противостояние')
            battle(question.__getattribute__(team), team)
        else:
            print('Отказ от противостояния')
            reconcile(question.__getattribute__(team), team)


def battle(team_ask, team_accept):

    num_ask = randint(1, 100)
    num_accept = randint(1, 100)
    print(f'team_1: {num_ask}, team_2: {num_accept}')
    if num_ask > num_accept:
        food[players.index(team_ask-1)] += 0.5*food[players.index(team_accept-1)]
        food[players.index(team_accept-1)] *= 0.5
    elif num_ask < num_accept:
        food[players.index(team_accept - 1)] += 0.5 * food[players.index(team_ask - 1)]
        food[players.index(team_ask - 1)] *= 0.5
    else:
        food[players.index(team_accept - 1)] += 50
        food[players.index(team_ask - 1)] += 50


def reconcile(team_ask, team_accept):
    food[players.index(team_accept)] *= 0.8
    people[players.index(team_ask)] *= 0.8


while running:
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
            case 2:
                team_2.do(square_colors[1], trace_colors[1])
            case 3:
                team_3.do(square_colors[2], trace_colors[2])
            case 4:
                team_4.do(square_colors[3], trace_colors[3])

        for i in range(1, 4 + 1):
            if i != current_team:
                pygame.draw.rect(screen, square_colors[i - 1], pygame.Rect(players[i - 1].x, players[i - 1].y, 10, 10))
                for point in players[i - 1].trace_points:
                    pygame.draw.rect(screen, trace_colors[i - 1], pygame.Rect(point[0], point[1], 1, 1))
    pygame.draw.circle(screen, 'blue', (270, 430), 10)
    pygame.display.update()

pygame.quit()


month = 1
while month < 8:
    month += 1
    current_team = 1
    resource_table = PrettyTable()
    resource_table.add_column('Команды', [1, 2, 3, 4])
    resource_table.add_column('Пропитание', food)
    resource_table.add_column('Экипаж', people)
    resource_table.add_column('Ценные находки', findings)
    resource_table.add_column('Средства защиты', protection_means)
    resource_table.add_column('Средства изучения', research_tools)
    print(resource_table)
    match current_team:
        case 1:
            alien_invasion(team_1)
            monthly_food(team_1)
            question(1)
            current_team += 1
        case 2:
            answer(2)
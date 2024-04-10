import pygame
from random import randint
from prettytable import PrettyTable
import ru_local as ru
import METEOR_RAIN
import STARVE
import random_events as ran

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


team_1 = Player(input(ru.NAME_TEAM1), 50, 50)
team_2 = Player(input(ru.NAME_TEAM2), 550, 550)
team_3 = Player(input(ru.NAME_TEAM3), 50, 550)
team_4 = Player(input(ru.NAME_TEAM4), 550, 50)

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
        print(ru.ALIEN_ATTACK)
        people[players.index(team)] *= 0.9
        defense[players.index(team)] *= 0.9
        print(ru.CREW, people[players.index(team)], ru.DEFENSE, defense[players.index(team)])


def monthly_food(team):
    food[players.index(team)] += 1000
    return food[players.index(team)]


rival_teams = [0] * 12


def question():
    global current_team, j
    if input(ru.DESIRE_CHALLENGE).lower() == ru.YES_NO:
        compete_team = int(input(ru.NUM_TEAM))
        while compete_team == current_team or compete_team > 4:
            print(ru.VALUE_ERROR)
            compete_team = int(input(ru.OTHER_VALUE))
        rival_teams[current_team - 1 + 4*j] = compete_team
        print(ru.TEAM, current_team, ru.CHALLENGED, compete_team)


def answer():
    global current_team, j
    for k in range(len(rival_teams)):
        if rival_teams[k] == current_team:
            if input(f'{ru.APPROVAL_TEAM} {current_team} {ru.BATTLE} {int((k+1) % 4) if (k+1) % 4 != 0 else int((k+5)/(j+1))}').lower() == ru.YES_NO:
                print(ru.FIGHT)
                battle()
            else:
                print(ru.NOT_FIGHT)
                reconcile()


def battle():
    global j
    num_ask = randint(1, 100)
    num_accept = randint(1, 100)
    print(ru.TEAM_CHELLENGE, num_ask, ru.SECOND_TEAM, num_accept)
    if num_ask > num_accept:
        food[rival_teams.index(current_team) - 4*j] += 0.5*food[current_team - 1]
        food[current_team - 1] *= 0.5
    elif num_ask < num_accept:
        food[current_team - 1] += 0.5 * food[rival_teams.index(current_team) - 4*j]
        food[rival_teams.index(current_team) - 4*j] *= 0.5
    else:
        food[current_team - 1] += 50
        food[rival_teams.index(current_team) - 4*j] += 50
    print(ru.RESOURCES_EQUAL, food[rival_teams.index(current_team) - 4*j],  food[current_team - 1])
    rival_teams[rival_teams.index(current_team)] = 0


def reconcile():
    global j
    food[current_team - 1] *= 0.8
    people[rival_teams.index(current_team) - 4*j] *= 0.8
    print(ru.RESOURCES_EQUAL, people[rival_teams.index(current_team) - 4*j], food[current_team - 1])
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
        print(ru.GAME_OVER)
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
                    print(ru.MOVE1)
                    food[0], people[0] = STARVE.starve(food[0], people[0])
                    defense[0], people[0] = METEOR_RAIN.meteor_rain(defense[0], people[0])
                    print(ru.CHANGE_FOOD, monthly_food(team_1))
                    ran.artifacts(findings[0], research_tools[0])
                    ran.sickness(people[0])
                    alien_invasion(team_1)
                    print(ru.INTERACTION_TEAM)
                    answer()
                    question()
                    bar_1.hp = people[0]/100
                    count_times += 1
            case 2:
                team_2.do(square_colors[1], trace_colors[1])
                if count_times == 1:
                    print(ru.MOVE2)
                    food[1], people[1] = STARVE.starve(food[1], people[1])
                    defense[1], people[1] = METEOR_RAIN.meteor_rain(defense[1], people[1])
                    ran.artifacts(findings[1], research_tools[1])
                    ran.sickness(people[1])
                    alien_invasion(team_2)
                    print(ru.CHANGE_FOOD, monthly_food(team_2))
                    print(ru.INTERACTION_TEAM)
                    answer()
                    question()
                    bar_2.hp = people[1] / 100
                    count_times += 1
            case 3:
                team_3.do(square_colors[2], trace_colors[2])
                if count_times == 2:
                    print(ru.MOVE3)
                    food[2], people[2] = STARVE.starve(food[2], people[2])
                    defense[2], people[2] = METEOR_RAIN.meteor_rain(defense[2], people[2])
                    print(ru.CHANGE_FOOD, monthly_food(team_3))
                    ran.artifacts(findings[2], research_tools[2])
                    ran.sickness(people[2])
                    alien_invasion(team_3)
                    print(ru.INTERACTION_TEAM)
                    answer()
                    question()
                    bar_3.hp = people[2] / 100
                    count_times += 1
            case 4:
                team_4.do(square_colors[3], trace_colors[3])
                if count_times == 3:
                    print(ru.MOVE4)
                    food[3], people[3] = STARVE.starve(food[3], people[3])
                    defense[3], people[3] = METEOR_RAIN.meteor_rain(defense[3], people[3])
                    print(ru.CHANGE_FOOD, monthly_food(team_4))
                    ran.artifacts(findings[3], research_tools[3])
                    ran.sickness(people[3])
                    alien_invasion(team_4)
                    print(ru.INTERACTION_TEAM)
                    answer()
                    question()
                    bar_4.hp = people[3] / 100
                    count_times = 0
                    resource_table = PrettyTable()
                    resource_table.add_column(ru.TEAMS, [1, 2, 3, 4])
                    resource_table.add_column(ru.FOODS, food)
                    resource_table.add_column(ru.CREW, people)
                    resource_table.add_column(ru.ARTEFACTS, findings)
                    resource_table.add_column(ru.DEFENSE, defense)
                    resource_table.add_column(ru.TOOLS, research_tools)
                    print(resource_table)
                    j += 1

        for i in range(1, 4 + 1):
            if i != current_team:
                pygame.draw.rect(screen, square_colors[i - 1], pygame.Rect(players[i - 1].x, players[i - 1].y, 10, 10))
                for point in players[i - 1].trace_points:
                    pygame.draw.rect(screen, trace_colors[i - 1], pygame.Rect(point[0], point[1], 1, 1))
    pygame.display.update()

pygame.quit()

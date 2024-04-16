import random

def meteor_rain(people, defense):
    meteor_chance = random.randint(1, 3)
    if meteor_chance == 1:
        if defense < 2000:
            print(f'На вас вас упал метеорит! Вы потеряли {people - int(people * 0.7)} людей.')
            return [int(people * 0.7), 0]
        else:
            print(f'На вас упал метеорит! Вы потеряли {defense * 0.5} защиты.')
            return [people, defense * 0.5]
    else:
        return [people, defense]
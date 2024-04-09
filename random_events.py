import random
people = 1000

def sickness():
    global people
    roulette_death = (200, 30, 80, 120, 5, 300)
    result_death = random.choice(roulette_death)
    roulette_failure = (1, 2, 3)
    result_failure = random.choice(roulette_failure)
    if result_failure == 1:
        print('Экипаж был заражён космической болезнью')
        people -= result_death
        print(people)

    return people

sickness()

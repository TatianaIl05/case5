import random
import ru_local


def meteor_rain(people, defense):
    '''
    This function triggers a random event in the form of a meteorite impact.
    :param people:
    :param defense:
    :return: people, defense
    '''
    meteor_chance = random.randint(1, 3)
    if meteor_chance == 1:
        if defense < 2000:
            print(f'{ru_local.METEORITE} {people - int(people * 0.7)} {ru_local.PEOPLES}')
            return [int(people * 0.7), 0]
        else:
            print(f'{ru_local.METEORITE} {defense * 0.5} {ru_local.DEFENSES2}')
            return [people, defense * 0.5]
    else:
        return [people, defense]

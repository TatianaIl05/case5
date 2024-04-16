import ru_local as ru
import random

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
    :param research_tools: number of research tools
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

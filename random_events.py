import ru_local as ru
import random
#findings = 0
#research_tools = 20

'''def sickness(people):
    
    #This function determines if the team gets sick.
    :param people: number of people in team
    :return: None
    
    roulette_death = (200, 30, 80, 120, 5, 300)
    result_death = random.choice(roulette_death)
    roulette_failure = (1, 2)
    result_failure = random.choice(roulette_failure)
    if result_failure == 1:
        print(f'({ru.DISEASE} {ru.LOST} {people} {ru.PEOPLES}))
        people -= result_death
        print(f'{ru.LOST} {people} {ru.PEOPLES}')

def artifacts(findings, research_tools):
    
    #This function determines whether the team finds a valuable artifact.
    :param findings: number of valuable artefacts
    :param research_tools: number of research tools
    :return: None
    
    items = (1, 2, 3, 5, 6, 7, 9)
    result_items = random.choice(items)
    if result_items % 2 == 0 or result_items == 3:
        print(ru.ARTEFACT)
        findings += 1
        if result_items == 2:
            research_tools += 30
            print(ru.FIND_ART, research_tools)
            print(ru.TOOLS, findings)
        elif result_items == 6:
            research_tools += 20
            print(ru.TOOLS, research_tools)
            print(ru.FIND_ART, findings)
        else:
            research_tools += 80
            print(ru.TOOLS, research_tools)
            print(ru.FIND_ART, findings)


sickness(1000) #Запуск случайного события - болезни
#artifacts(0, 560) #Запуск случайного события - ценные артефакты'''
#-----------------------------------------------------------------
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
    items = (1, 2, 4, 3, 6, 7, 9)
    result_items = random.choice(items)
    if result_items % 2 == 0 or result_items == 3:
        print(ru.ARTEFACT)
        findings += 1
        '''if result_items == 2:
            research_tools += 30
            print(ru.TOOLS, research_tools)
            print(ru.FIND_ART, findings)
        elif result_items == 6:
            research_tools += 20
            print(ru.TOOLS, research_tools)
            print(ru.FIND_ART, findings)
        else:
            research_tools += 80
            print(ru.TOOLS, research_tools)
            print(ru.FIND_ART, findings)'''
    else:
        print('Команда не смогла найти артефакты')
    return findings


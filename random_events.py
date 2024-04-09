import ru_local as ru
import random
people = 1000
findings = 0
research_tools = 20

def sickness():
    global people
    roulette_death = (200, 30, 80, 120, 5, 300)
    result_death = random.choice(roulette_death)
    roulette_failure = (1, 2, 3)
    result_failure = random.choice(roulette_failure)
    if result_failure == 1:
        print(ru.DISEASE)
        people -= result_death

    return people

def artifacts():
    global findings
    global research_tools
    items = (1, 2, 3, 5, 6, 7, 9)
    result_items = random.choice(items)
    if result_items % 2 == 0 or result_items == 3:
        print(ru.ARTEFACT)
        findings += 1
        if result_items == 2:
            research_tools += 30
        elif result_items == 6:
            research_tools += 20
        else:
            research_tools += 80

    return findings, research_tools

sickness() #Запуск случайного события - болезни
artifacts() #Запуск случайного события - ценные артефакты

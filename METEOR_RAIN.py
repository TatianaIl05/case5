#
import random


def case_if_check():
    avaliable_meteor_check = str(random.randint(1, 2))
    if avaliable_meteor_check == '1':
        global meteor_chance
        meteor_chance = random.randint(1, 2)
        match meteor_chance:
            case 1:
                print('There is a meteor danger')
            case 2:
                print('There is no meteor danger')
            # case _:
            #     print('Неверно введено значение')
            #     case_if_check()
    else:
        print('The weather is too bad to analise')


def case_if_stay_go():
    print('Do you want to stay there or go to another place?', '\n', 'press 1 - stay, press 2 - go', '\n')
    match int(input()):
        case 1:
            print('Despite the risk you stayed')
            return True
        case 2:
            print('You have gone to another place. God protects those who are careful')
            return False
        case _:
            print('Неверно введено значение')
            case_if_stay_go()


def aware():
    print('Do you want to check meteor activity?', '\n', 'press 1 - yes, press 2 - no')
    a = str(input())
    if a == '1':
        return case_if_check()
    elif a == '2':
        print('хозяин - барин')
        return case_if_stay_go()
    else:
        print('wrong value')
        aware()



def meteor_rain(defence, stuff):
    if aware() == True and int(meteor_chance) == 1:
        meteor_damage_chance = random.randint(1, 2):
        if


meteor_rain(2, 4)
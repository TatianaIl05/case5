#
import random


def case_if_check():
    avaliable_meteor_check = str(random.randint(1, 2))
    if avaliable_meteor_check == '1':
        meteor_chance = random.randint(1, 2)
        match meteor_chance:
            case 1:
                print('There is a meteor danger')
            case 2:
                print('There is no meteor danger')
            case _:
                print('Неверно введено значение')
                case_if_check(x)
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
    if str(input()) == '1':
        case_if_check()
    if int(input()) == 2:
        print('press enter')
    else:
        print('press enter')
        aware()
    return case_if_stay_go()

aware()

# def meteor_rain(defence, stuff):
#     aware()

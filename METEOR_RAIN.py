#
import random


def case_if_check():
    avaliable_meteor_check = str(random.randint(1, 2))
    if avaliable_meteor_check == '1':
        match meteor_chance:
            case 1:
                print('There is a meteor danger')
                case_if_stay_go()
            case 2:
                print('There is no meteor danger')
                case_if_stay_go()
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
    global meteor_chance
    meteor_chance = random.randint(1, 2)
    if a == '1':
        return case_if_check()
    elif a == '2':
        print('хозяин - барин')
        return case_if_stay_go()
    else:
        print('wrong value')
        aware()


def meteor_rain(defence, stuff):
    aware_ = aware()
    print()
    if aware_ == True and int(meteor_chance) == 1:
        meteor_damage_chance = random.randint(1, 2)
        if int(meteor_damage_chance) == 1:
            if defence >= 20:
                defence = defence // 2
            elif defence < 20:
                defence = 0
            elif defence == 0:
                stuff = stuff // 3
        else:
            print('The meteor rain have ran other side. Lucky you')
        return [defence, stuff]
    elif aware_ == True and int(meteor_chance) == 2:
        print(f'You stayed on location, what will be next?')
        return [defence, stuff]
    # elif aware == None and int(meteor_chance) == 1:

    else:
        return [defence, stuff]


# meteor_rain(2, 4)

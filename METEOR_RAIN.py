#
import random


def case_if_check():
    avaliable_meteor_check = str(random.randint(1, 2))
    if avaliable_meteor_check == '1':
        match meteor_chance:
            case 1:
                print('Существует метеоритная опасность')
                case_if_stay_go()
            case 2:
                print('Метеоритной опасности нет')
                case_if_stay_go()
    else:
        print('Погода слишком плохая, чтобы анализировать ситуацию')
        case_if_stay_go()


def case_if_stay_go():
    print('Вы хотите остаться там или поехать в другое место?', '\n', 'нажмите 1 - остаться, нажмите 2 - перейти', '\n')
    match int(input()):
        case 1:
            print('Несмотря на риск, ты остался')
            return 1
        case 2:
            print('Вы ушли в другое место. Бог хранит тех, кто осторожен')
            return 2
        case _:
            print('Неверно введено значение')
            case_if_stay_go()


def aware():
    print('Вы хотите проверить метеорную активность?', '\n', 'нажмите 1 - да, нажмите 2 - нет')
    a = str(input())
    global meteor_chance
    meteor_chance = random.randint(1, 2)
    if a == '1':
        return case_if_check()
    elif a == '2':
        print('хозяин - барин')
        return case_if_stay_go()
    else:
        print('неправильное значение')
        aware()


def meteor_rain(defence, stuff):
    aware_ = aware()
    if (aware_ == 1 and int(meteor_chance) == 1) or (aware is None and int(meteor_chance) == 1):
        meteor_damage_chance = random.randint(1, 2)
        if int(meteor_damage_chance) == 1:
            if defence >= 20:
                defence = defence // 2
            elif defence < 20:
                defence = 0
            elif defence == 0:
                stuff = stuff // 3
        else:
            print('Метеоритный дождь прошел с другой стороны. Повезло тебе')
        return [defence, stuff]
    elif (aware_ == 2 and int(meteor_chance) == 2) or (aware_ is None and int(meteor_chance) == 2):
        print(f'Вы остались на месте, что будет дальше?')
        return [defence, stuff]
    # elif aware == None and int(meteor_chance) == 1:

    else:
        return [defence, stuff]


# meteor_rain(2, 4)

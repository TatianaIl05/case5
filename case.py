def case(people, ar, attack, defense, food, flag=None):
    '''
    This function offers the team a choice of action
    in its turn. From a random event to non-random ones.
    :param people:
    :param ar:
    :param attack:
    :param defense:
    :param food:
    :param flag:
    :return: None
    '''
    print('Что будем делать?', '\n' '1. улучшить атаку', '\n' '2. улучшить защиту', '\n' '3. Исследовать территорию', '\n' '4. Купить еду')
    var = int(input())
    match var:
        case 1:
            ar += 0.3
            print(f'Вы улучшили атаку. Теперь она {attack * ar}')
            return [people, ar, defense, food, flag, ]
        case 2:
            defense += 200
            print(f'Вы улучшили защиту. Теперь она {defense}')
            return [people, ar, defense, food, flag]
        case 3:
            flag = 'red'
            return [people, ar, defense, food, flag]
        case 4:
            print(f'Вы купили еду. Теперь у вас {food + 6000} еды')
            return [people, ar, defense, food + 6000, flag]
        case _:
            print('Неверное значение')
            case()

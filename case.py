import ru_local as ru


def case(people, ar, attack, defense, food, flag=0):
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
    print(
        f'{ru.CHOOSING_ACTION} \n {ru.CHOICE_ATTACK} \n {ru.CHOICE_DEFENSE} \n {ru.CHOICE_LOCATION} \n {ru.CHOICE_FOOD}')
    var = int(input())
    while var not in [1, 4]:
        print(ru.MISTAKE)
        var = int(input())
    match var:
        case 1:
            ar += 0.3
            print(f'{ru.UPGRADE_ATTACK} {attack * ar}')
            return [people, ar, defense, food, flag, ]
        case 2:
            defense += 200
            print(f'{ru.UPGRADE_DEFENSE} {defense}')
            return [people, ar, defense, food, flag]
        case 3:
            flag = ru.RED
            return [people, ar, defense, food, flag]
        case 4:
            print(f'{ru.UPGRADE_FOOD} {food + 6000} {ru.FOOD1}')
            return [people, ar, defense, food + 6000, flag]
        # case _:
        #     print(ru.MISTAKE)
        #     case(people, ar, attack, defense, food, flag=0)

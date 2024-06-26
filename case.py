import ru_local as ru


def case(people, ar, attack, defense, food, flag=None):
    '''
    This function offers the team a choice of action
    in its turn. From a random event to non-random ones.
    :param people: people count
    :param ar: ar
    :param attack: attack count
    :param defense: defense count
    :param food: food count
    :param flag: flag
    :return: None
    '''
    print(f'{ru.CHOOSING_ACTION} \n {ru.CHOICE_ATTACK} \n {ru.CHOICE_DEFENSE} \n {ru.CHOICE_LOCATION} '
          f'\n {ru.CHOICE_FOOD}')
    var = int(input())
    match var:
        case 1:
            ar += 0.3
            print(f'{ru.UPGRADE_ATTACK} {attack * ar}')
            return [people, ar, attack, defense, food, flag]
        case 2:
            defense += 200
            print(f'{ru.UPGRADE_DEFENSE} {defense}')
            return [people, ar, attack, defense, food, flag]
        case 3:
            flag = ru.RED
            return [people, ar, attack, defense, food, flag]
        case 4:
            print(f'{ru.UPGRADE_FOOD} {food + 6000} {ru.FOOD1}')
            return [people, ar, attack, defense, food + 6000, flag]
        case _:
            print(ru.MISTAKE)
            return case(people, ar, attack, defense, food, flag=None)

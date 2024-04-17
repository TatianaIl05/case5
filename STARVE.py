import ru_local


def starve(food, people, usage):
    '''
    This function declares hunger when the food value of the team is low.
    :param food:
    :param people:
    :param usage:
    :return: [food - usage, people, people * 0.5]
    '''
    if usage > food:
        print(f'{ru_local.HUNGER} {int(abs(food - usage))} {ru_local.PEOPLES}')
        return [0, people - abs(food - usage), (people - abs(food - usage)) * 0.5]
    else:
        return [food - usage, people, people * 0.5]

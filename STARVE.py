# def rep_func(x, y, z):
#     if x == y:
#         return True
#     if x == z:
#         return False
#     else:
#         print('wrong value')
#         rep_func(x, y, z)
#
#
# def check_food(food):
#     print('Check food?', '\n', '1 - yes | 2 - no')
#     var = int(input())
#     ans = rep_func(var, 1, 2)
#     if ans:
#         print(f'you have {food} food before step')
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


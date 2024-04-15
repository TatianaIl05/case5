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


def starve(food, people, usage):
    # check_food(food)
    if usage > food:
        print(f'Starvation. You have lack of food. You lost {int(abs(food - usage))} people')
        return [0, people - abs(food - usage), (people - usage) * 0.5]
    else:
        return [food - usage, people, people * 0.5]


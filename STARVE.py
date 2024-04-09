def rep_func(x, y, z):
    if x == y:
        return True
    if x == z:
        return False
    else:
        print('wrong value')
        rep_func(x, y, z)


def check_food(food):
    print('Check food?', '\n', '1 - yes | 2 - no')
    var = int(input())
    ans = rep_func(var, 1, 2)
    if ans:
        print(f'you have {food} food before step')


def starve(food, stuff):
    check_food(food)
    if stuff * 0.5 > food:
        print(f'Starvation. You have lack of food. You lost {int(abs(food - stuff * 0.5))} stuff')
        return [0, int(stuff - abs(food - stuff))]
    else:
        return [int(food - stuff * 0.5), stuff]


starve(10, 45)

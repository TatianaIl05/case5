def case(people, ar, attack, defense, food, flag=None):
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
            print(f'Вы купили еду. Теперь у вас {food + 800}')
            return [people, ar, defense, food + 8000, flag]
        case _:
            print('Неверное значение')
            case()

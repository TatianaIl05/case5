from prettytable import PrettyTable

food = [14000, 14000, 14000, 14000]
people = [7000, 7000, 7000, 7000]
attack = [100, 100, 100, 100]
research_tools = [20, 20, 20, 20]
defense = [50, 50, 50, 50]
def start_info():
    print(f'Ход {step + 1} команды {team + 1}')
    table_columns = ['Люди', 'Еда', 'Защита', 'Атака']
    table = PrettyTable(table_columns)
    table.add_row([people[team], food[team], defense[team], attack[team]])
    print(table)

for step in range(4):
    for team in range(4):
        start_info()

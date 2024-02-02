'''
+ поле из 9 клеток
+ игрок_1 - X
+ игрок_2 - 0
игроки ходят по очереди
начинает X
победа:
    3 одинаковых по горизонтали, вертикали или диагонали
ничья - нет свободны клеток и нет победителя
'''


def draw_filed(field: list) -> None:
    ''' Выводит на экран три ряда игрового поля '''
    for i in range(0, 7, 3):
        print(field[i], field[i + 1], field[i + 2])


def make_move(field: list, player: str):
    '''
    Спрашивает номер клетки поля: 1-9 вкл
    Проверяет, есть ли на поле клетка с таким номером
    Проверяет, что клетка с этим номером свободна
    Если пройдет все проерки, ставит игрока в эту клетку
    '''
    while True:
        cell_num = int(input('Введите номер клетки (1-9): '))
        if cell_num < 1 or cell_num > 9:
            print('Ошибка! Номер должен быть от 1 до 9 вкл.')
            continue
        if field[cell_num - 1] in players:
            print('Ошибка! Эта клетка занята.')
            continue
        field[cell_num - 1] = player
        break


player_1 = 'X'
player_2 = '0'
players = (player_1, player_2)
field = list(range(1, 10, 1))
moves = 1

while True:
    if moves > 9:
        print('Ничья')
        break
    draw_filed(field)
    if moves % 2:
        make_move(field, player_1)
    else:
        make_move(field, player_2)
    moves += 1


print('Игра окончена.')

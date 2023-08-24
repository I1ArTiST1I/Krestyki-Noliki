BOARD = {7: '_', 8: '_', 9: '_', 4: '_', 5: '_', 6: '_',
         1: '_', 2: '_', 3: '_'}

PLAYERS = {
    'X': [],
    'O': []
}

WIN_RULES = (
    (7, 8, 9),
    (4, 5, 6),
    (1, 2, 3),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (3, 5, 7),
    (1, 5, 9)
)


def print_board():
    print(f'{BOARD[7]} {BOARD[8]} {BOARD[9]}')
    print(f'{BOARD[4]} {BOARD[5]} {BOARD[6]}')
    print(f'{BOARD[1]} {BOARD[2]} {BOARD[3]}')


def win_check(sign):
    board_mask = set(PLAYERS[sign])
    winner = bool([True for rule in WIN_RULES if len(
        board_mask.intersection(rule)) == 3])
    return winner


def set_cell(cell, sign):
    BOARD[cell] = sign
    PLAYERS[sign].append(cell)


def start():
    sign = 'X'
    step = 1
    while True:
        print_board()

        cell = input(
            f'\nИгрок за {sign}, введите ячейку [1-9] или 0 для продолжения игры: ')

        if cell == '0':
            break

        elif cell in list(map(str, range(1, 10))):
            if BOARD[int(cell)] == '_':
                set_cell(int(cell), sign)
            else:
                print(f'\nЯчейка занят... повторите ввод')
                continue
            if win_check(sign):
                print(f'\nИгрок за {sign} победитель!!!')
                print_board()
                break
            else:
                if step == 9:
                    print(f'\nБольше никаких шагов. Игра окончена. Ничья!')
                    print_board()
                    break
                else:
                    step += 1
            sign = 'O' if sign == 'X' else 'X'

        else:
            print(
                '\nНеправильный ввод: должно быть [1-9] для выбранной ячейки или 0 для выхода из игры')
            continue


if __name__ == '__main__':
    print(f'\n Добро пожаловать в "Крестики-Нолики" ')
    print(f'Ваша задача по очереди заполнять поля X и O, использую NumPad. Хорошой игры)\n')
    start()

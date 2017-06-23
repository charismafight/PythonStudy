import random
import os
import msvcrt

# another decorate of act in actions
# actions is ge key='Q' value=func in actions dict
actions = {}

# score
default_score = random.randrange(2, 5, 2)
# random row and col to select a position
game_data = [[0 for x in range(4)] for r in range(4)]
game_data[random.randrange(0, 3)][random.randrange(0, 3)] = default_score


# game_data = [[0, 4, 0, 0], [0, 4, 0, 0], [2, 4, 0, 0], [0, 8, 0, 0]]


def command(command_key):
    def switch_func(f):
        # set actions and return func
        actions[command_key] = f
        return f

    return switch_func


# decorate of command validate,do validate first then call specified func
# this decorate should be put behind 'command' because it must be invoke after actions has filled
def validate(func):
    def validate_input(c):
        if str.upper(c) in actions:
            func(c)
        else:
            print('invalid input:' + c)

    return validate_input


# a decorate to generate a num into some blank
def generator(func):
    def wrapper():
        func()
        if contain_zero(game_data):
            # find all 0 pos
            for i, r in enumerate(game_data):
                for j, col in enumerate(r):
                    if col == 0:
                        game_data[i][j] = random.randrange(2, 5, 2)
                        return
        else:
            # game over
            print('game over')
            exit(0)

    return wrapper


def contain_zero(table):
    for x in table:
        for y in x:
            if y == 0:
                return True
    return False


# command invoker
@validate
def do_command(k):
    f = actions[k]
    f()


@command('Q')
def quit_game():
    print('see u next time!')
    exit(0)


@command('R')
def restart_game():
    global game_data
    print('restart！')
    game_data = [[0 for x in range(4)] for r in range(4)]
    game_data[random.randrange(0, 3)][random.randrange(0, 3)] = random.randrange(2, 5, 2)
    update_screen()


@command('A')
@generator
# @generator
def left():
    for x in range(len(game_data)):
        # maybe need a recursion func
        game_row_handler(game_data[x])
    return


@command('D')
@generator
def right():
    for x in range(len(game_data)):
        game_data[x].reverse()
        game_row_handler(game_data[x])
        game_data[x].reverse()


@command('W')
@generator
def up():
    global game_data
    result = list(map(game_row_handler, list(map(list, zip(*game_data)))))
    # row trans col
    game_data = list(map(list, zip(*result)))


@command('S')
@generator
def down():
    global game_data
    game_data_afterzip = list(map(list, zip(*game_data)))
    for r in game_data_afterzip: r.reverse()
    list(map(game_row_handler, game_data_afterzip))
    # row trans col
    for r in game_data_afterzip: r.reverse()
    game_data = list(map(list, zip(*game_data_afterzip)))


def game_row_handler(row):
    for i in range(len(row)):
        pos = i
        if i == 0:
            continue
        # if left num is 0 then move until i-n = 0
        if row[i - 1] == 0:
            pos = move_left(row, i)

        # combine when moved
        if row[pos] == row[pos - 1]:
            row[pos - 1], row[pos] = row[pos] * 2, 0

        if row[i - 1] != row[i]:
            continue
    return row


def move_left(row, i):
    # record the pos of i,it may be changed when move
    pos = i
    if i == 0 or row[i] == 0:
        return pos
    # if the num before it is 0 then change their position
    if row[i - 1] == 0:
        row[i], row[i - 1] = 0, row[i]
        pos = move_left(row, i - 1)

    return pos


# give default score to a random 0 position
def update_screen():
    clear_screen()
    score = max(map(max, *game_data))
    print('Score:' + str(score))
    # checkerboard
    sides = '+-----------------------+'
    blanks = '|{0}|{1}|{2}|{3}|'

    # loop array to fill blanks
    print(sides)
    for i in range(4):
        print(blanks.format(*[str(o).rjust(5).replace('    0', '     ') for o in game_data[i]]))
        print(sides)
    # description
    print('(W) up  (S) down  (A) left  (D) right  (R) reset  (Q) exit')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# ini update
update_screen()

while True:
    code = msvcrt.getch().decode()
    # deal with input
    do_command(str.upper(code))
    update_screen()

# # test
# do_command('W')
# do_command('A')
# update_screen()

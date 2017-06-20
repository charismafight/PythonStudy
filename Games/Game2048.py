import random
import os
import msvcrt

# another decorate of act in actions
# actions is ge key='Q' value=func in actions dict
actions = {}

# score
default_score = random.randrange(2, 5, 2)
# random row and col to select a position
row = random.randrange(0, 3)
col = random.randrange(0, 3)
# game_data = [[0 for x in range(4)] for r in range(4)]
# game_data[row][col] = default_score
game_data = [[2, 4, 0, 0], [0, 2, 0, 0], [0, 4, 0, 0], [0, 8, 0, 0]]


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
        if True in [0 in x for x in game_data]:
            while True:
                num = random.randrange(2, 5, 2)
                r_row = random.randrange(0, 3)
                r_col = random.randrange(0, 3)
                if game_data[r_row][r_col] == 0:
                    game_data[r_row][r_col] = num
                    break
        else:
            # game over
            print('game over')
            exit(0)

    return wrapper


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
    print('restart！')
    default_score = random.randrange(2, 5, 2)
    game_data = [[0 for x in range(4)] for r in range(4)]
    row = random.randrange(0, 3)
    col = random.randrange(0, 3)
    game_data[row][col] = default_score
    return


@command('A')
#@generator
def left():
    for x in range(len(game_data)):
        # maybe need a recursion func
        game_row_handler(game_data[x])
    return


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


@command('D')
def right():
    for x in range(len(game_data)):
        game_data[x].reverse()
        game_row_handler(game_data[x])
        game_data[x].reverse()


# give default score to a random 0 position

def update_screen():
    os.system('cls')
    score = default_score
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


# ini update
update_screen()

# while True:
#     code = msvcrt.getch().decode()
#     # deal with input
#     do_command(str.upper(code))
#     update_screen()

# test
do_command('D')
update_screen()

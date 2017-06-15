import random
import msvcrt

# another decorate of act in actions
# actions is ge key='Q' value=func in actions dict
actions = {}

# score
default_score = random.randrange(2, 5, 2)
# random row and col to select a position
row = random.randrange(0, 3)
col = random.randrange(0, 3)
game_data = [[0 for x in range(4)] for r in range(4)]
game_data[row][col] = default_score


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
@generator
def left():
    for x in range(len(game_data)):
        # maybe need a recursion func
        game_row_left_handler(game_data[x])
    return


@command('D')
def right():
    for x in range(-4, -1):
        game_row_right_handler(game_data[x])



def game_row_left_handler(row):
    for i in range(len(row) - 1):
        if i == 0:
            continue
        # if left num is 0 then move until i-n = 0
        if row[i - 1] == 0:
            move_left(row, i)
            continue
        if row[i - 1] != row[i]:
            continue

        if row[i] == row[i - 1]:
            row[i - 1], row[i] = row[i] * 2, 0
    #print(game_data)


def move_left(row, i):
    if i == 0 or row[i] == 0:
        return
    if row[i - 1] == 0:
        row[i], row[i - 1] = 0, row[i]
        move_left(row, i - 1)


@generator
def game_row_right_handler(row):
    for i in range(-len(row)):
        if i == 1:
            continue
        # if left num is 0 then move
        if row[i] == 0:
            row[i], row[i + 1] = row[i + 1], row[i]
            continue
        if row[i] != row[i + 1]:
            continue

        if row[i] == row[i + 1]:
            row[i], row[i + 1] = row[i + 1] * 2, 0


# give default score to a random 0 position

def update_screen():
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

#while True:
    # code = msvcrt.getch().decode()
    # deal with input
code = 'A'
do_command(str.upper(code))
update_screen()

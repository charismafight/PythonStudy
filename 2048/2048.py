import random as r
import msvcrt


# decorate of command validate,do validate first then call specified func
def validate(func):
    def validate_input(c):
        if str.upper(c) in commands:
            func(c)
        else:
            print('invalid input:' + c)

    return validate_input


# another decorate of act in actions
# actions is ge key='Q' value=func in actions dict
actions = {}


def command(command_key):
    def switch_func(f):
        # set actions and return func
        actions[command_key] = f
        return f

    return switch_func


def do_command(k):
    f = actions[k]
    f(k)


@validate
@command('Q')
def quit_game(v_code):
    exit(0)


@validate
@command('R')
def restart_game(v_code):
    return


# score
firstNum = r.randrange(2, 5, 2)
score = firstNum
print('Score:' + str(score))
# checkerboard

# description
print('(↑) up  (↓) down  (←) left  (→) right  (R) reset  (Q) exit')
commands = ['R', 'Q']

while True:
    code = msvcrt.getch().decode()
    # deal with input
    do_command(str.upper(code))

import random as r
import msvcrt

# another decorate of act in actions
# actions is ge key='Q' value=func in actions dict
actions = {}


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
    return


# score
firstNum = r.randrange(2, 5, 2)
score = firstNum
print('Score:' + str(score))
# checkerboard
print()

# description
print('(W) up  (S) down  (A) left  (D) right  (R) reset  (Q) exit')

while True:
    code = msvcrt.getch().decode()
    # deal with input
    do_command(str.upper(code))

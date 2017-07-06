from pygame import *
import sys

init()

size = width, height = 800, 600
speed = [1, 1]
black = 0, 0, 0

screen = display.set_mode(size)

p = sys.path[0]
ball = image.load(p + '/pics/intro_ball.gif')
ball_rect = ball.get_rect()

while 1:
    for e in event.get():
        if e.type == QUIT:
            exit(0)
    ball_rect = ball_rect.move(speed)
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(ball, ball_rect)
    display.flip()

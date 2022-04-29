from turtle import Screen
from line import Line
from board import Board
from ball import Ball
from scoreboard import Scoreboard

import time

WIDTH = 1200
HEIGHT = 800

screen = Screen()

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title('Pong Arcade Game')
screen.tracer(0)

line = Line()
ball = Ball()

screen.listen()

player1 = Board((550,0))
player2 = Board((-550,0))

score1 = Scoreboard((100,350))
score2 = Scoreboard((-100,350))

screen.onkey(player1.up, 'Up')
screen.onkey(player1.down, 'Down')

screen.onkey(player2.up, 'w')
screen.onkey(player2.down, 's')


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    line.mid_line()
    ball.move()
    
    #DETECT COLLISION WITH THE BOARDS
    if ball.distance(player1) < 40 and ball.xcor() > 520 or ball.distance(player2) < 40 and ball.xcor() < -520:  
        ball.bounce_x() 
    
    #DETECT COLLISION WITH THE WALLS
    if ball.ycor() > 350 or ball.ycor() < -350:
        #BOUNCE THE BALL    
        ball.bounce_y()    
    if ball.xcor() > 580:
        ball.reset()
        score2.increase_score()
    if ball.xcor() < -580:
        ball.reset()
        score1.increase_score()
    

screen.exitonclick()
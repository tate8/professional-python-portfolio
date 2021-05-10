from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from object import Object
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=500, height=700)
screen.title('Breakout')

objects = []

paddle = Paddle((0, -300))
x = -280
y = 320


for _ in range(4):
    for _ in range(8):
        x += 60
        obj = Object((x, y))
        objects.append(obj)
    x = -280
    y -= 30
    
ball = Ball()
sb = Scoreboard()
tt = Scoreboard()
start_time = time.time()

# keypress
screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')



game_on = True
while game_on == True:
    ball.move()

    # ball vs. edges
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()
    if ball.xcor() > 230 or ball.xcor() < -230:
        ball.bounce_x()
    # ball vs. bottom
    if ball.ycor() < -330:
        print('ball bottom')
        ball.hideturtle()
        ball.x_move = 0
        ball.y_move = 0
        sb.game_over()
    # ball vs. paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -290:
        ball.bounce_y()
    # ball vs. objects
    for obj in objects:
        if ball.distance(obj) < 20:
            ball.bounce_y()
            obj.health -= 100
            if obj.health == 0:
                objects.remove(obj)
                obj.hideturtle()
                del obj
                print('gone')
    # if all objects r gone, you win
    if len(objects) == 0:
        print(len(objects))
        ball.hideturtle()
        ball.x_move = 0
        ball.y_move = 0
        sb.game_won()
        tt.time_taken(start_time)
        game_on = False





















screen.exitonclick()
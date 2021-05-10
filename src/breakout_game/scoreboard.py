from turtle import Turtle
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.pu()
        self.write('Game Over', align='center', font=('Courier', 80, 'normal'))

    def game_won(self):
        self.goto(0, 0)
        self.pu()
        self.write('You Won!', align='center', font=('Courier', 80, 'normal'))
    
    def time_taken(self, start_time):
        self.goto(0, -50)
        end_time = time.time()
        time_taken = int(end_time - start_time)
        self.pu()
        self.write(f'in {time_taken} scs', align='center', font=('Courier', 24, 'normal'))
from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
FORWARD = 20

class Board(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(position)  
        
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
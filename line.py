from turtle import Turtle

FORWARD = 20

class Line(Turtle):
    
    def __init__(self):
        super().__init__()
        self.positions = []
        self.x_cor = 0
        self.y_cor = 0
        self.vertical_coor()
        
    def vertical_coor(self):
        for self.y_cor in range(400, -400, -20):
            pos = (self.x_cor,self.y_cor)
            self.positions.append(pos)
            
    def mid_line(self):
        for x in self.positions:
            self.shape('arrow')
            self.color('white')
            self.setheading(270)
            self.penup()
            self.goto(x)
            self.pendown()
            self.forward(FORWARD)
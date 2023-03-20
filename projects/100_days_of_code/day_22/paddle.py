from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.x = position[0]
        self.y = position[1]
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.penup()
        self.goto(self.x, self.y)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
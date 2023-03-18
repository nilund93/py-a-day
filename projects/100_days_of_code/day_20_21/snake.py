from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    
    MOVE_DISTANCE = 20
    
    def __init__(self) -> None:
        self.body = []
        self.initialize()
        self.head = self.body[0]
    
    def initialize(self):
        x = 0
        for _ in range(3):
            temp_turtle = Turtle(shape="square")
            temp_turtle.color("white")
            temp_turtle.penup()
            temp_turtle.goto(x, 0)
            self.body.append(temp_turtle)
        x-=20
        
    def move(self):
        for seg_num in range(len(self.body)-1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.head.forward(self.MOVE_DISTANCE)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)    

class Food:
    
    def __init__(self) -> None:
        pass
    
class Scoreboard:
    
    def __init__(self) -> None:
        pass
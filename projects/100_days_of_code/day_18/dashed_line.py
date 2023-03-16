from turtle import Turtle

dashed = Turtle()
dashed.shape("arrow")
dashed.color("red")

for _ in range(5):
    dashed.pendown()
    dashed.forward(15)
    dashed.penup()
    dashed.forward(15)
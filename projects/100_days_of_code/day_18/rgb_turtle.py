import turtle as t
from random import choice, randint

# thicker lines
# speed up the turtle
# 

ANGLES = [0, 90, 180, 270]
kevin = t.Turtle()
kevin.shape("arrow")
kevin.speed(10)
kevin.pensize(20)
kevin.color("black")
t.colormode(255)
kevin.width(5)

def random_color():
    rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
    kevin.color(rgb)

def random_walk():
    random_color()

    paces = randint(15, 60)
    kevin.setheading(choice(ANGLES))
    kevin.forward(paces)


if __name__ == "__main__":
    for _ in range(100):
        random_walk()
    input()
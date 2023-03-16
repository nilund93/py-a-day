from turtle import Turtle
from random import choice, randint

# thicker lines
# speed up the turtle
# 

COLORS = ["cyan", "cadet blue", "crimson", "light coral", "indigo", "gold", "beige", "sky blue", "pale goldenrod"]
ANGLES = [0, 90, 180, 270]
kevin = Turtle()
kevin.shape("arrow")
kevin.speed = 10
kevin.color = "black"
kevin.pensize = 20

def random_walk():
    kevin.color = choice(COLORS)

    paces = randint(15, 60)
    kevin.setheading(choice(ANGLES))
    kevin.forward(paces)


if __name__ == "__main__":
    for _ in range(100):
        random_walk()
    input()
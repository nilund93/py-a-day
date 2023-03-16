import turtle as t
from random import randint

spiro = t.Turtle()
spiro.shape("arrow")
t.colormode(255)
spiro.speed("fastest")

def random_color():
    rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
    return rgb

def spirograph(size: int):
    # my solution
    
    for _ in range(36):
        spiro.color(random_color())
        spiro.circle(size)
        spiro.left(10)

def angela_spiro(size_of_gap: int):
    # Angelas solution
    
    for _ in range(int(360/size_of_gap)):
        spiro.color(random_color())
        spiro.circle(100)
        spiro.setheading(spiro.heading() + size_of_gap)

if __name__ == "__main__":
    spirograph(60)
    angela_spiro(5)
    input()
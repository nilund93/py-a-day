from turtle import Turtle
from random import choice

geo = Turtle()
colors = ["cyan", "cadet blue", "crimson", "light coral", "indigo", "gold", "beige", "sky blue", "pale goldenrod"]

def static_sizes():
    geo.shape("turtle")
    geo.color("red")

    # square
    for _ in range(4):
        geo.forward(30)
        geo.left(90)
        
    input()

    # pentagon
    geo.color("blue")
    for _ in range(5):
        geo.forward(40)
        geo.left(72)
        
    input()

    # hexagon

    geo.color("magenta")
    for _ in range(6):
        geo.forward(50)
        geo.left(60)

    input()

def generic_size(sides: int):
    
    angle = 360 / sides
    geo.color(choice(colors))
    
    for _ in range(sides):
        geo.forward(70)
        geo.left(angle)
    
    input()
    
if __name__ == "__main__":
    #static_sizes()
    for i in range(4, 12):
        generic_size(i)
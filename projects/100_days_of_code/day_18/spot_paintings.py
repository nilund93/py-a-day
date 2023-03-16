import turtle as t
import colorgram
from random import choice

painter = t.Turtle()
painter.shape("arrow")
t.colormode(255)

def hirst_image(hirst_colors):
    # dots size 20
    # size apart 50
    
    for i in range(11):
        painter.setpos(0, 50*i)
        painter.setheading(0)
        for __ in range(10):
            painter.color(choice(hirst_colors))
            painter.pendown()
            painter.dot(20)
            painter.penup()
            painter.forward(50)
            painter.pendown()
        painter.penup()
            
    

if __name__ == "__main__":
    # extract all the colors from the image
    colors_from_picture = colorgram.extract("hirst.jpg", 30)
    
    colors = []
    for color in colors_from_picture:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        colors.append((r, g, b))
    
    #print(colors)
    hirst_image(colors)
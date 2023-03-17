from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
is_race_on = False

def initialize_turtles(participating_turtles: list()):
    for turtle in participating_turtles:
        #turtle.color(random_color())
        turtle.shape("turtle")
    
def create_turtles():
    turtles = []
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        turtles.append(new_turtle)
    
    return turtles
    
def init_turtles(turtles):
    y = 75
    for turtle in turtles:
        turtle.penup()
        turtle.goto(x=-230, y = y)
        y -= 25

def race(participants):
    for turtle in participants:
        speed = randint(0, 10)
        turtle.pendown()
        turtle.forward(speed)
        if turtle.xcor() >= 230:
            return False, turtle.pencolor()
    return True, ""
                

if __name__ == "__main__":
    
    user_bet = screen.textinput("Make your bet!", "Which turtle will win the race? Enter a color: ")
    if user_bet:
        turtles = create_turtles()
        init_turtles(turtles)
        is_race_on = True
    
    winning_color = ""
    while is_race_on:
        is_race_on, winning_color = race(turtles)
    
    print(f"{winning_color} won!")
    if user_bet == winning_color:
        print("You won the wager!")
    else:
        print("You lost the wager.")    
    
    
    screen.exitonclick()
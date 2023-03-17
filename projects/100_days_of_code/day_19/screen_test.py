from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

if __name__ == "__main__":
    screen.listen()
    screen.onkey(key="space", fun=move_forwards)
    screen.exitonclick()
    

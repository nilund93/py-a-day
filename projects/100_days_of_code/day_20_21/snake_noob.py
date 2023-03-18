from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on = True
snake = []

def initialize_snake(snake):
    x = 0
    for _ in range(3):
        temp_turtle = Turtle(shape="square")
        temp_turtle.color("white")
        temp_turtle.penup()
        temp_turtle.goto(x, 0)
        snake.append(temp_turtle)
        x-=20
    return snake

if __name__ == "__main__":
    snake = initialize_snake(snake)
    screen.update()
    
    while game_is_on:
        screen.update()
        time.sleep(0.1)
            
        for seg_num in range(len(snake)-1, 0, -1):
            new_x = snake[seg_num - 1].xcor()
            new_y = snake[seg_num - 1].ycor()
            snake[seg_num].goto(new_x, new_y)
        snake[0].forward(20)
        snake[0].left(90)
        snake[0].forward(20)
            
        
        
        
screen.exitonclick()
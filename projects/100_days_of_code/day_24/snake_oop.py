from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
    
if __name__ == "__main__":    
    
    game_is_on = True
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    
    
    
    while game_is_on:
        
        # Update screen and move snake every tick.
        screen.update()
        time.sleep(0.1)
        snake.move()
        
        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
        
        # Detect collision with walls.
        if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -280:
            scoreboard.reset()
            snake.reset()
            
        # Detect collision with self.
        for segment in snake.body[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()
                        
    screen.exitonclick()
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Turtle Crossing")
screen.tracer(0)

player_turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_turtle.move, "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    if player_turtle.check_win():
        car_manager.increase_speed()
        # car_manager.cars.append(car_manager.create_car())
        scoreboard.next_level()
    
    for car in car_manager.cars:
        if player_turtle.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    
screen.exitonclick()

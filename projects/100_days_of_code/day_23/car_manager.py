from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.movement_speed = STARTING_MOVE_DISTANCE
    
    def create_cars(self, amount: int):
        for _ in range(amount):            
            (self.create_car())
    
    def create_car(self):
        chance = randint(1,6)
        if chance == 1:
            temp_car = Turtle(shape="square")
            temp_car.shapesize(stretch_wid=1, stretch_len=3)
            temp_car.color(choice(COLORS))
            temp_car.penup()
            temp_car.goto(300, randint(-240, 260))
            temp_car.setheading(180)
            self.cars.append(temp_car)
            
    def check_cars(self):
        for car in self.cars:
            if car.xcor() < -600:
                car.goto(600, randint(-240, 260))
    
    def move_cars(self):
        for car in self.cars:
            car.forward(self.movement_speed)
    
    def increase_speed(self):
        self.movement_speed += MOVE_INCREMENT 

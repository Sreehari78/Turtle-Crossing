from turtle import Turtle
from random import randint, choice


COLORS = ["red", "orange", "yellow", "green", "blue", "violet"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance % 2 == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(choice(COLORS))
            random_y = randint(-300, 300)
            random_x = randint(250, 700)
            car.goto(random_x, random_y)
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT

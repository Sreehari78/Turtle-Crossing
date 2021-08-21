import time
from turtle import Screen
from cars import Cars
from player import Player
from scoreboard import Score

screen = Screen()
screen.setup(width=1366, height=700)
screen.listen()
screen.tracer(0)

car_manager = Cars()
user = Player()
level = Score()


screen.onkey(user.up, "Up")
screen.onkey(user.down, "Down")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.2)
    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if user.distance(car) < 25:
            level.game_over()
            is_game_on = False

    # Detect a successful crossing
    if user.level_completion():
        car_manager.increase_car_speed()
        level.level_up()

    # Detect game completion
    if level.current_level > 11:
        level.game_completion()
        is_game_on = False

screen.exitonclick()

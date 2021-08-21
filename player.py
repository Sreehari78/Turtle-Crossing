from turtle import Turtle

STARTING_POSITION = (0, -330)
MOVEMENT_SPEED = 10
FINISH_LINE_Y = 330


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("green")
        self.penup()
        self.goto_start_line()

    def goto_start_line(self):
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVEMENT_SPEED)

    def down(self):
        self.backward(MOVEMENT_SPEED)

    def level_completion(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto_start_line()
            return True
        else:
            return False

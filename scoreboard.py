from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")
WINNING_POSITION = (0, 0)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-600, 330)
        self.hideturtle()
        self.current_level = 1
        self.level_up()

    def level_up(self):
        self.clear()
        self.write(f"Level : {self.current_level}", align=ALIGNMENT, font=FONT)
        self.current_level += 1

    def game_completion(self):
        self.clear()
        self.goto(WINNING_POSITION)
        self.write(f"CONGRATULATIONS!! YOU WON!", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(WINNING_POSITION)
        self.write(f"SPLASHHH!!! GAME OVER!", align=ALIGNMENT, font=FONT)

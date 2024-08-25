FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Initialize the score
        self.penup()  # Lift the pen to avoid drawing when moving
        self.hideturtle()  # Hide the turtle shape (just show the text)
        self.goto(-280, 260)
        self.level=0
        self.update_scoreboard()  # Display the initial score

    def update_scoreboard(self):
        self.clear()
        self.level+=1
        self.goto(-280, 260)
        self.write(f"Level = {self.level}", True, align="left",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", True, align="center",font=FONT)


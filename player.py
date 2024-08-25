from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()


    def create_player(self):
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def up(self):
        new_y = self.ycor() + 20
        if new_y<FINISH_LINE_Y :  # Prevent moving off the screen
            self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        if self.ycor() >= 260:
            return True
        else:
            return False
    def go_to_start (self):
        self.goto(STARTING_POSITION)


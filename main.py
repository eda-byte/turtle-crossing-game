import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("yellow")
screen.tracer(0)
player=Player()
#car=CarManager()
screen.listen()
screen.onkey(player.up,"Up")
car = CarManager()
scoreboard=Scoreboard()
#scoreboard.update_scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.cars_go()
    for carr in car.all_cars:
        if player.distance(carr)<20:
            scoreboard.game_over()
            game_is_on=False

        if player.is_at_finish_line()==True:
            player.go_to_start()
            car.increase_speed()
            scoreboard.update_scoreboard()
            break

   # for i in range (1,50):
        #if i%6==
    #    car.cars_go()

screen.exitonclick()
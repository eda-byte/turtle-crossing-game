from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        #self.create_cars()
        self.all_cars=[]
        self.cars_go()
        self.car_speed = STARTING_MOVE_DISTANCE  # Initialize the car speed

    def create_car(self):
      #  global cars
        random_chance=random.randint(1,6)
        if random_chance==6:
            colors = ["red", "blue", "green", "yellow", "purple", "orange"]  # List of possible colors
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(colors))
            new_car.shapesize(1,2)
            new_car.penup()
            #random_x = random.randint(-300, 300)
            random_y = random.randint(-250, 250)

            new_car.goto(280,random_y)
               # self.cars_go()
            self.all_cars.append(new_car)

    def cars_go(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
           # self.all_cars[car].forward(MOVE_INCREMENT)

    def increase_speed(self):
        for car in self.all_cars:
            self.car_speed+=MOVE_INCREMENT
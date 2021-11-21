from turtle import Turtle
from random import choice, randint, randrange

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car():

    def __init__(self):
        self.all_cars = []
        self.car_reserve = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            if self.car_reserve:
                new_car = self.car_reserve.pop()
            else:
                new_car = Turtle('square')
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_car.up()
                new_car.color(choice(COLORS))
            random_y_position = randrange(-230, 230, 20)
            new_car.goto(320, random_y_position)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor() < -320:
                self.all_cars.remove(car)
                self.car_reserve.append(car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

from turtle import Turtle
from barrier import BarrierManager
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.shapesize(0.5)
        self.color("purple")

    def get_random_location(self):
        ran_x = random.randint(-270,270)
        ran_y = random.randint(-270,270)
        loc_tuple = (ran_x, ran_y)
        return loc_tuple

    def relocate(self, barriers, random_position):
        food_location = random_position
        try: # try because in the beginning there are no barriers
            for barrier in barriers:
                while barrier.distance(food_location) < 15:
                    food_location = self.get_random_location()
        except: # in the cases there isn't a barrier
            food_location = self.get_random_location()
        print(f"food location: {food_location}")
        self.goto(food_location)
        # try:
        #     food_location = random_position # self.get_random_location()
        #     while barrier.distance(food_location) < 15:
        #         food_location = self.get_random_location()
        # except:
        #     food_location = self.get_random_location()
        # print(f"food location: {food_location}")
        # self.goto(food_location)

from turtle import Turtle, Screen
import time

SNAKE_STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        self.tail = self.snake_segments[-1]

    def create_snake(self):
        for positions in SNAKE_STARTING_POSITIONS:
            self.add_segment(positions)

    def move(self):
        for seg_number in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[seg_number].goto(self.snake_segments[seg_number - 1].position())

        self.snake_segments[0].forward(20)

    def add_segment(self, positions):
        body_seg = Turtle(shape="square")
        body_seg.color("white")
        body_seg.penup()
        body_seg.goto(positions)
        self.snake_segments.append(body_seg)

    def extend(self):
        self.add_segment(self.snake_segments[-1].pos())

    def reset_snake(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        self.tail = self.snake_segments[-1]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def dn(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def lt(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def rt(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
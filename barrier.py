from turtle import Turtle


class BarrierManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.barriers = []

    def create_barrier(self, position):
        print(f"Barrier created, pos: {position}")
        barrier = Turtle(shape="square")
        barrier.color("white")
        barrier.penup()
        self.barriers.append(barrier)
        barrier.goto(position)

    def reset_barriers(self):
        for barrier in self.barriers:
            barrier.goto(1000, 1000)
        self.barriers.clear()

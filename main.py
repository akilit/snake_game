from turtle import Turtle, Screen
import barrier
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game!")
my_screen.tracer(0)

snake = Snake()
scoreboard = Scoreboard()
barrierManager = barrier.BarrierManager()
food = Food()
food.relocate(0, food.get_random_location())

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.dn, "Down")
my_screen.onkey(snake.rt, "Right")
my_screen.onkey(snake.lt, "Left")

isOn = True
while isOn:
    my_screen.update()
    time.sleep(.1)

    if snake.head.distance(food) < 15:
        print("food eaten")
        scoreboard.plusone()
        barrierManager.create_barrier(snake.tail.pos())
        food.relocate(barrierManager.barriers, food.get_random_location)
        # for barrier in barrierManager.barriers:
        #     food.relocate(barrier, food.get_random_location()) # doesn't actually do anything with the second parameter
        snake.extend()


    # wall-collision detector
    if snake.head.xcor() > 350 or snake.head.xcor() < -350 or snake.head.ycor() < -350 or snake.head.ycor() > 350:
        scoreboard.update_screen()
        barrierManager.reset_barriers()
        snake.reset_snake()
    # 280, -280, -280, 280
    # snake-collision detector
    for segment in snake.snake_segments[3::]:
        if snake.head.distance(segment) <= 15:
            scoreboard.update_screen()
            snake.reset_snake()

    # snake-barrier detector
    for barrier in barrierManager.barriers:
        if snake.head.distance(barrier) < 15:
            print("barrier collision")
            snake.reset_snake()
            scoreboard.update_screen()
            barrierManager.reset_barriers()

    snake.move()

my_screen.exitonclick()

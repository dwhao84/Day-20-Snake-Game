# Create a snake body
# Move the snake
# Control the snake
# Detect collision with food
# Create a scoreboard
# Detect collision with the wall
# Detect collision with tail

from turtle import Turtle, Screen
import time
from turtledemo.penrose import start

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # Make animation

starting_positions = [(-20,0), (-40,0), (0,0)]
segments = [ ]

for position in starting_positions:
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # Delay, slow down.
    
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x =segments[seg_num - 1].xcor()
        new_y =segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
        
    segments[0].forward(20)
    segments[0].left(20)
screen.exitonclick()

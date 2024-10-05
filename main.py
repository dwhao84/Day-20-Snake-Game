# Create a snake body
# Move the snake
# Control the snake
# Detect collision with food
# Create a scoreboard
# Detect collision with the wall
# Detect collision with tail

from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # Make animation

snake = Snake()  # Call snake game.
food = Food()
scoreboard = Scoreboard()

screen.listen()  # 監聽
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # Refresh the screen
    time.sleep(0.1)  # Delay, slow down.
    snake.move()     # Call snake in Snake case.
    
    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh() # refresh食物的位置。
        snake.extend() # 蛇吃到食物後，會長胖
        print("nom nom nom")
        scoreboard.increase_scoreboard() # 計分板增加
        
    # Detect collision with wall
    # 用if else設定條件，當snake的頭超過x軸的280、小於x軸 -280 或者 snake的頭的y軸大於280 或者 snake的頭的y軸小於 -280
    # 結果要印出 Game Over，並將遊戲停止。
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print("Game Over")
        game_is_on = False
        scoreboard.game_over()
    
    # Detect collision with tail
    for segment in snake.segments[1:]: # 使用Slice語法。
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    
screen.exitonclick()

"""
1. Snake -> Create the snake class
2. Food
3. Scoreboard
"""
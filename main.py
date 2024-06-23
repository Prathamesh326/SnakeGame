from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        # snake.extend += 1
        snake.grow()
        score.calculate_score()

    # detect collision wit wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.gameover()

    # detect collision with the tail
    for segment in snake.all_snake[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.gameover()

screen.exitonclick()

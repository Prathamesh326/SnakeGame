import turtle as t

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_snake = []
        self.extend = 3
        self.create_snake()
        self.head = self.all_snake[0]

    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            self.add_segment(position)

        # for i in range(self.extend):
        #     self.add_segment()

    def add_segment(self, position):
        snake = t.Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.all_snake.append(snake)
        # X = 0
        # snake = t.Turtle("square")
        # snake.color("white")
        # snake.penup()
        # snake.goto(X, 0)
        # self.all_snake.append(snake)
        # X -= 20

    def grow(self):
        self.add_segment(self.all_snake[-1].position())

    def move_snake(self):
        for i in range(len(self.all_snake) - 1, 0, -1):
            new_x = self.all_snake[i - 1].xcor()
            new_y = self.all_snake[i - 1].ycor()
            self.all_snake[i].goto(new_x, new_y)
        self.all_snake[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

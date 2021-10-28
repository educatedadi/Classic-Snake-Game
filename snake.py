from turtle import Turtle

STARTING_X_POSITION = 0
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


def generate_turtle():
    new_turtle = Turtle()
    new_turtle.shape('square')
    new_turtle.color('white')
    new_turtle.penup()
    return new_turtle


class Snake:
    def __init__(self):
        self.all_turtles = []
        x_position = STARTING_X_POSITION
        for index_num in range(3):
            new_turtle = generate_turtle()
            new_turtle.goto(x=x_position, y=0)
            self.all_turtles.append(new_turtle)
            x_position -= 20
        self.head = self.all_turtles[0]

    def add_body(self):
        """Add a segment to the snake's body"""
        new_turtle = generate_turtle()
        new_turtle.goto(self.all_turtles[-1].position())
        self.all_turtles.append(new_turtle)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):
        """Moves the snake in forward direction"""
        segments = len(self.all_turtles) - 1
        for i in range(len(self.all_turtles)):
            if segments == 0:
                self.all_turtles[segments].forward(MOVE_DISTANCE)
            else:
                new_x = self.all_turtles[segments - 1].xcor()
                new_y = self.all_turtles[segments - 1].ycor()
                self.all_turtles[segments].goto(new_x, new_y)
            segments -= 1

    def check_wall_collision(self):
        """"Check if the snakes get collided with the screen"""
        if self.head.xcor() > 280 or self.head.xcor() < -280 or \
                self.head.ycor() > 280 or self.head.ycor() < -280:
            return False
        else:
            return True

    def loops_back_to_screen(self):
        """When the snake gets out of the screen then this makes it come out from the other side"""
        for segment in self.all_turtles:
            if segment.xcor() < -300 or segment.xcor() > 300:
                segment.goto(-segment.xcor(), segment.ycor())

            elif segment.ycor() < -300 or segment.ycor() > 300:
                segment.goto(segment.xcor(), -segment.ycor())
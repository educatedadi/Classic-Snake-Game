from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score


def switch_on():
    global game_is_on, did_respond
    game_is_on = True
    did_respond = True


def switch_off():
    global did_respond, is_looping
    did_respond = True
    is_looping = False


is_looping = True
while is_looping:

    canvas = Screen()
    canvas.title('My Snake Game')
    canvas.setup(width=600, height=600)
    canvas.bgcolor('black')
    canvas.tracer(0)

    snake = Snake()
    food = Food()
    score = Score()
    canvas.listen()

    game_is_on = False
    did_respond = False

    # Checks if user has responded to prompts or not
    while not did_respond:
        score.ask_to_play()
        canvas.onkey(key='space', fun=switch_on)
        canvas.onkey(key='e', fun=switch_off)

    while game_is_on:
        canvas.update()
        time.sleep(0.1)
        snake.move()
        score.update()

        # Detects if a key is pressed to move the snake
        canvas.onkey(key='Up', fun=snake.move_up)
        canvas.onkey(key='Down', fun=snake.move_down)
        canvas.onkey(key='Right', fun=snake.move_right)
        canvas.onkey(key='Left', fun=snake.move_left)

        # Detects collision with the food
        if snake.head.distance(food) < 15:
            food.new_food()
            score.increases()
            snake.add_body()

        # Detects collision with the Wall
        # game_is_on = snake.check_wall_collision()
        
        # TO SWITCH B/W LEVELS THEN COMMENT OUT ONE LINE, EITHER ABOVE⬆(game_is_on) OR BELOW⬇(snake.loops...)
        
        # Loops back from other side of screen if gets outside of the screen
        snake.loops_back_to_screen()

        # Check collision with the tail
        for body_part in snake.all_turtles[1:]:
            if snake.head.distance(body_part) < 10:
                game_is_on = False

        # Prints GAME OVER
        if not game_is_on:
            score.game_over()
            time.sleep(2)

    canvas.clearscreen()

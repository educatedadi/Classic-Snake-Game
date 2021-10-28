from turtle import Turtle

SCORE_FONTS = ('Arial', 18, 'bold')
GAME_OVER_FONT = ('Chunq', 24, 'bold')
ASK_FOR_COMMAND_FONT = ('Courier', 14, 'bold')

highest_score = 0


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.score_board = 'SCORE :\t' + str(self.current_score)
        self.color('White')
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(0, 260)
        self.write(self.score_board, False, align='center', font=SCORE_FONTS)

    def increases(self):
        self.current_score += 1
        self.score_board = 'SCORE :\t' + str(self.current_score)

    def game_over(self):
        global highest_score
        if self.current_score > highest_score:
            highest_score = self.current_score
        self.goto(0, 235)
        self.write(f'Highest Score:  {highest_score}', False, align='center', font=SCORE_FONTS)
        self.home()
        self.write('GAME OVER!', False, align='center', font=GAME_OVER_FONT)

    def ask_to_play(self):
        self.goto(0, -100)
        self.write('Press SPACEBAR to play the game! \nor E to exit!', False, align='center', font=ASK_FOR_COMMAND_FONT)
        self.clear()


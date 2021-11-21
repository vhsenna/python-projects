from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 14, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('snake_game/data/data.txt') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.up()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.score} | High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('snake_game/data/data.txt'', 'w') as data:
                data.write(f'{self.high_score}')
        self.clear()
        self.score = 0
        self.update_score()

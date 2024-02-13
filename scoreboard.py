from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("White")
        self.hideturtle()
        self.printscore()

    def printscore(self):
        self.write(f"Score: {self.score} Highscore: {self.get_data()}", move=False, align="center", font= ("Times New Roman", 24, "normal"))

    def plusone(self):
        self.score += 1
        self.clear()
        self.printscore()

    def record_data(self):
        with open("../../Desktop/data.txt", mode="w") as high_score_file:
                high_score_file.write(self.highscore.__str__())

    def get_data(self):
        try:
            with open("../../Desktop/data.txt") as high_school_file:
                contents = int(high_school_file.read())
            return contents
        except ValueError:
            return 0

    def update_screen(self):
        if self.score > self.get_data():
            self.highscore = self.score
            self.record_data()
        self.score = 0
        self.clear()
        self.printscore()

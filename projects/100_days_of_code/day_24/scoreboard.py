from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
POSITION = (0, 265)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.fetch_highscore()
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def fetch_highscore(self):
        with open("data.txt", mode="r", encoding="utf-8") as f:
            self.high_score = int(f.read())
    
    def save_highscore(self):
        with open("data.txt", mode="w", encoding="utf-8") as f:
            f.write(str(self.high_score))
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_highscore()
        self.score = 0
        self.update_scoreboard()
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
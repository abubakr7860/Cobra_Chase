from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score=0
        
        with open("data.txt")as data:
            self.high_score=int(data.read())
        self.penup()
        self.goto(x=0,y=270)
        self.clear()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}","High Score:{self.high_score}",align="center",font=("Courier",15,"normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open ("data.txt",mode="w")as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()

    
    def inc_score(self):
        self.score+=1
        self.update_scoreboard()



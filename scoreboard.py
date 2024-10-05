from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
    
    # 計分板加分。
    def increase_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.score += 1
        self.update_scoreboard()
        
    # 在視窗視角上方，更新計分板。
    def update_scoreboard(self):
        self.write(f"Score: { self.score } ", True, align= ALIGN, font= FONT )
    
    # 在視窗視角上方，寫入Game Over
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", True, align= ALIGN, font= FONT )
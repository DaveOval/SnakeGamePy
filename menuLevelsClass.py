import turtle
from ScrfeenClass import Scrfeen

class levelMenu:
    def __init__(self, scrfeen, backMethod, initGameMethod):
        self.pantalla = scrfeen.window
        self.screen = scrfeen

        self.leves = ["easy", "medium", "hard"]

        self.selected_level = None
        self.current_level = 0

        self.backMethod = backMethod
        self.initGameMethod = initGameMethod

        self.title = turtle.Turtle()
        self.title.speed(0)
        self.title.color("white")
        self.title.penup()
        self.title.goto(0, 250)
        self.title.hideturtle()

        self.title.write("Menu level", align="center", font=("Courier", 24, "normal"))

        self.level_text = turtle.Turtle()
        self.level_text.speed(0)
        self.level_text.color("white")
        self.level_text.penup()
        self.level_text.goto(0, 210)
        self.level_text.hideturtle()
        self.level_text.write("Select a game level:", align="center", font=("Courier", 24, "normal"))

        self.add_back_button()

        self.buttons = []
        for i, option in enumerate(self.leves):
            button = turtle.Turtle()
            button.speed(0)
            button.color("white")
            button.penup()
            button.goto(0, -i * 100)
            button.write(option, align="center", font=("Courier", 24, "normal"))
            button.hideturtle()
            self.buttons.append(button)



        self.selector = turtle.Turtle()
        self.selector.speed(0)
        self.selector.color("yellow")
        self.selector.penup()
        self.selector.goto(0, 0)
        self.selector.shape("square")
        self.selector.shapesize(stretch_wid=1, stretch_len=5)

        self.pantalla.listen()  
        self.update_selector()
        self.pantalla.onkeypress(self.move_up, "Up")
        self.pantalla.onkeypress(self.move_down, "Down")
        self.pantalla.onkeypress(self.change_level, "Return")


    def add_back_button(self):
        back_button = turtle.Turtle()
        back_button.speed(0)
        back_button.color("white")
        back_button.penup()
        back_button.hideturtle()
        back_button.goto(-260, 260)
        back_button.write("<", align="center", font=("Courier", 24, "normal"))

    def update_selector(self):
        x = self.buttons[self.current_level].xcor()
        y = self.buttons[self.current_level].ycor() - 10
        self.selector.goto(x, y)

    def move_up(self):
        if self.current_level > 0:
            self.current_level -= 1
            self.update_selector()
    
    def move_down(self):
        if self.current_level < len(self.leves) - 1:
            self.current_level += 1
            self.update_selector()

    def change_level(self):
        self.selected_level = self.leves[self.current_level]
        self.pantalla.clear()
        if self.selected_level == "easy":
            self.initGameMethod(0.3)
        elif self.selected_level == "medium":
            self.initGameMethod(0.2)
        elif self.selected_level == "hard":
            self.initGameMethod(0.1)
        else:
            self.initGameMethod(0.2)


def back():
    print("back")
def initGame(level):
    print(level)
    print("initGame")

window = Scrfeen(600, 600, "Level Menu", "black")
levelMenu = levelMenu(window, back, initGame)
turtle.mainloop()


import turtle
from ScrfeenClass import Scrfeen

class Snake:
    def __init__(self, headColor, bodyColor):
        self.segmentos = []

        self.head = turtle.Turtle()
        self.head.speed(0)

        self.head.shape('square')
        self.head.color(headColor)

        self.head.penup()
        self.head.goto(0, 0)

        self.head.direction = 'stop'

        self.bodyColor = bodyColor

    def controls(self, window, up, down, left, right):
        window.listen()
        window.onkeypress(self.up, up)
        window.onkeypress(self.down, down)
        window.onkeypress(self.left, left)
        window.onkeypress(self.right, right)


    def up(self):
        print("up")
        if self.head.direction != 'down':
            self.head.direction = 'up'

    def down(self):
        print("down")
        if self.head.direction != 'up':
            self.head.direction = 'down'
    
    def left(self):
        print("left")
        if self.head.direction != 'right':
            self.head.direction = 'left'

    def right(self):
        print("right")
        if self.head.direction != 'left':
            self.head.direction = 'right'

scrfeen = Scrfeen(600, 600, "Snake", "black")
scrfeen.setArena(400, "red", True)
snake = Snake("white", "white")
snake.controls(scrfeen.window, "w", "s", "a", "d")
scrfeen.window.update()
turtle.mainloop()


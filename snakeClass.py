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
    def move(self, screen):
        if self.head.direction == 'up':
            y = self.head.ycor()
            if y < ((screen.height/2) - 20):
                self.head.sety(y + 20)
            else:
                print("You lose")

        if self.head.direction == 'down':
            y = self.head.ycor()
            if y > -(screen.height/2):
                self.head.sety(y - 20)
            else:
                print("You lose")
        
        if self.head.direction == 'left':
            x = self.head.xcor()
            if x > -(screen.width/2):
                self.head.setx(x - 20)
            else:
                print("You lose")
        
        if self.head.direction == 'right':
            x = self.head.xcor()
            if x < (screen.width/2) :
                self.head.setx(x + 20)
            else:
                print("You lose")
    
    def addSegment(self):
        self.newSegment = turtle.Turtle()
        self.newSegment.speed(0)
        self.newSegment.shape('square')
        self.newSegment.color(self.bodyColor)
        self.newSegment.penup()
        self.segmentos.append(self.newSegment)

    def moveBody(self):
        lenght = len(self.segmentos)
        for i in range( lenght - 1, 0, -1):
            x = self.segmentos[i - 1].xcor()
            y = self.segmentos[i - 1].ycor()
            self.segmentos[i].goto(x, y)
        if lenght > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.segmentos[0].goto(x, y)

    def colision(self):
        for segment in self.segmentos:
            if self.head.distance(segment) < 20:
                print("You lose")
                break

scrfeen = Scrfeen(600, 600, "Snake", "black")
scrfeen.setArena(400, "red", True)
snake = Snake("white", "white")
snake.controls(scrfeen.window, "w", "s", "a", "d")

def gameLoop():
    snake.move(scrfeen)
    if snake.head.direction != 'stop':
        snake.addSegment()  
    snake.colision()
    scrfeen.window.update()
    scrfeen.window.ontimer(gameLoop, 100)
    snake.moveBody()

gameLoop()
turtle.mainloop()


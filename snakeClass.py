import turtle
from ScrfeenClass import Scrfeen
import time

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

    def move(self, game ,screen):
        if self.head.direction == 'up':
            y = self.head.ycor()
            if y < ((screen.height/2) - 20):
                self.head.sety(y + 20)
            else:
                game.loose = True
                print("You lose")

        if self.head.direction == 'down':
            y = self.head.ycor()
            if y > -(screen.height/2):
                self.head.sety(y - 20)
            else:
                game.loose = True
                print("You lose")
        
        if self.head.direction == 'left':
            x = self.head.xcor()
            if x > -(screen.width/2):
                self.head.setx(x - 20)
            else:
                game.loose = True
                print("You lose")
        
        if self.head.direction == 'right':
            x = self.head.xcor()
            if x < (screen.width/2) :
                self.head.setx(x + 20)
            else:
                game.loose = True
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

    def colision(self, game):
        for segment in self.segmentos:
            if self.head.distance(segment) < 20:
                game.loose = True
                print("You lose")
                break

class Game():
    loose = False
    score = 0
    max_score = 0

    def __init__(self, delay = 0.2):
        self.delay = delay


    def displayScore(self, textColor):
        self.texto = turtle.Turtle()
        self.texto.speed(0)
        self.texto.color(textColor)
        self.texto.penup()
        # self.texto.hideturtle()
        self.texto.goto(0, 250)
        self.texto.write('Score: 0 Max Score: 0', align='center', font=('times', 24, 'normal'))

    def updateScore(self, score):
        self.score += score
        if self.score > self.max_score:
            self.max_score = self.score
        self.texto.clear()
        text_content = 'Score: {} Max Score: {}'.format(self.score, self.max_score)
        self.texto.write( text_content , align='center', font=('times', 24, 'normal'))

    def resetScore(self):
        self.score = 0
        self.texto.clear()
        self.texto('white')
        self.texto.goto(0, 250)
        text_content = 'Score: {} Max Score: {}'.format(self.score, self.max_score)
        self.texto.write( text_content , align='center', font=('times', 24, 'normal'))

    def gamerOver(self, screen):
        self.texto.clear()
        self.texto.color('red')
        self.texto.write('GAME OVER', align='center', font=('times', 40, 'bold'))
        screen.window.update()
        time.sleep(2)

    def toDefeat(self, snake, screen):
        self.loose = False
        self.gamerOver(screen)
        snake.head.direction = 'stop'
        snake.head.goto(0, 0)
        for seg in snake.segmentos:
            seg.hideturtle()
            snake.segmentos.clear()
        self.resetScore()


game = Game()
scrfeen = Scrfeen(600, 600, "Snake Game", "black")
scrfeen.setArena(400, "red", False)
snake = Snake('green', 'white')

snake.controls(scrfeen.window, 'w', 's', 'a', 'd')

game.displayScore('white')

def upload():
    if game.loose == True:
        game.toDefeat(snake, scrfeen)
    else:
        snake.move(game, scrfeen)
        if snake.head.direction != 'stop':
            snake.addSegment()
            snake.colision(game)
            game.updateScore(1)

    scrfeen.window.update()
    snake.moveBody()
    scrfeen.window.ontimer(upload, 100)

upload()
scrfeen.window.mainloop()


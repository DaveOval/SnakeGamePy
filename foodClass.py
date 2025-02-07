import turtle
import random
from snakeClass import Snake

class Food():
    def __init__(self, foodColor, screen):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape('circle')
        self.food.color(foodColor)
        self.food.penup()

        self.food.goto(0, 40)
        self.side = screen.side

    def collision(self, snake, game):
        if snake.head.distance(self.food) < 20:
            condition = True

            while condition:
                x = ( random.randint( 0 , 19 ) * 20 ) - (self.side / 2)
                y = ( random.randint( 0 , 19 ) * 20 ) - (self.side / 2)

                if len(snake.segmentos) > 0:
                    for segment in snake.segmentos:
                        if x == segment.xcor() and y == segment.ycor():
                            condition = True
                            break
                        else:
                            condition = False
                else:
                    condition = False
            self.food.goto(x, y)
            game.updateScore(10)
            snake.addSegment()
            
            return True
        else:
            return False
        
    def resetFood(self):
        self.food.goto(0, 40)
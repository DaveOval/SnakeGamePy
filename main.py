from ScrfeenClass import Scrfeen
from snakeClass import Snake
from snakeClass import Game
from foodClass import Food

import time

game = Game(0.2)

game.displayScore('white')

window = Scrfeen(600, 600, 'Snake game' ,'black') 

window.setArena(400, 'red', False)

snake = Snake('green', 'gray')
snake.controls(window.window, 'w', 's', 'a', 'd')

food = Food('blue', window)

while game.running:
    window.window.update()
    if game.loose:
        game.toDefeat(snake, window, food)
    if food.collision(snake, game):
        food.collision(snake, game)
        snake.moveBody()
        continue
    snake.moveBody()
    snake.move(game, window)
    snake.colision(game, window, food)
    time.sleep(game.delay)
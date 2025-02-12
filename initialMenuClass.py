import turtle
from PIL import Image

class InitialMenu:
    def __init__( self, scrfeen):
        self.window = scrfeen.window
        self.screen = scrfeen
        self.options = ['Start', 'Score', 'About']

        self.selected_option = None

        self.current_option = 0

        self.title = turtle.Turtle()
        self.title.speed(0)
        self.title.color('white')
        self.title.penup()
        self.title.goto(0, 250)
        self.title.write('Snake Game', align='center', font=('Courier', 36, 'bold'))
        self.title.hideturtle()

        self.subtitle = turtle.Turtle()
        self.subtitle.speed(0)
        self.subtitle.color('white')
        self.subtitle.penup()
        self.subtitle.goto(0, 210)
        self.subtitle.write('Select an option', align='center', font=('Courier', 24, 'normal'))
        self.subtitle.hideturtle()


        self.redimensionar_imagen('imag.png', 'img_resize.png', 100, 100)

        self.window.addshape('img_resize.png')

        self.img = turtle.Turtle()
        self.img.speed(0)
        self.img.penup()
        self.img.shape('img_resize.png')
        self.img.goto(0, 100)

        self.buttons = []

        for i, option in enumerate(self.options):
            button = turtle.Turtle()
            button.speed(0)
            button.color('white')
            button.penup()
            button.goto(0, -i * 100)
            button.write(option, align='center', font=('Courier', 24, 'normal'))
            button.hideturtle()
            self.buttons.append(button)

        self.selector = turtle.Turtle()
        self.selector.speed(0)
        self.selector.penup()
        self.selector.color('yellow')
        self.selector.shape('square')
        self.selector.shapesize( stretch_wid=1, stretch_len=10 )

        self.window.listen()
        self.move_selector()
        self.window.onkey(self.move_up, 'Up')
        self.window.onkey(self.move_down, 'Down')

    def move_selector(self):
        x = self.buttons[self.current_option].xcor()
        y = self.buttons[self.current_option].ycor() - 10
        self.selector.goto(x, y)

    def redimensionar_imagen(self, origin_path, destination_path, width, height):
        image = Image.open(origin_path)
        new_image = image.resize((width, height))
        new_image.save(destination_path)

    def move_up(self):
        if self.current_option > 0:
            self.current_option -= 1
            self.move_selector()
        
    def move_down(self):
        if self.current_option < len(self.options) - 1:
            self.current_option += 1
            self.move_selector()


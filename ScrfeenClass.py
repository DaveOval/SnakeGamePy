import turtle


class Scrfeen:
    def __init__(self, width, height, title ,background):
        self.window = turtle.Screen()
        self.window.title(title)
        self.window.bgcolor(background)

        self.width = width  # Agregar esta línea
        self.height = height  # Agregar esta línea

        self.window.setup(width=width, height=height)
        self.window.tracer(0)


        canvas = self.window.getcanvas()
        root = canvas.winfo_toplevel()
        def on_close():
            print("Closing")
            self.window.bye()

        root.protocol("WM_DELETE_WINDOW", on_close)
    def setArena(self, side, borderColor, grid = False):
        self.side = side
        self.borderColor = borderColor

        if grid:
            ver = turtle.Turtle()
            hor = turtle.Turtle()
            ver.speed(0)
            hor.speed(0)

            ver.hideturtle()

            ver.goto(-(self.side / 2)-10, -(self.side / 2)-10)
            ver.color('white')
            ver.left(90)

            for i in range(10):
                ver.forward(self.side)
                ver.right(90)
                ver.forward(20)
                ver.right(90)
                ver.forward(self.side)
                ver.left(90)
                ver.forward(20)
                ver.left(90)

            hor.hideturtle()

            hor.goto(-(self.side / 2)-10, -(self.side / 2)-10)
            hor.color('white')

            for i in range(10):
                hor.forward(self.side)
                hor.left(90)
                hor.forward(20)
                hor.left(90)
                hor.forward(self.side)
                hor.right(90)
                hor.forward(20)
                hor.right(90)
        arena = turtle.Turtle()

        arena.speed(0)
        arena.hideturtle()
        arena.goto(-(self.side / 2)-10, -(self.side / 2)-10)
        arena.color(self.borderColor)
        for i in range(4):
            arena.forward(self.side)
            arena.left(90)

        self.window.update()
                
""" scrfeen = Scrfeen(600, 600, "My Game", "black")
scrfeen.setArena(400, "red", True)
turtle.mainloop() """
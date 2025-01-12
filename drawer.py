import turtle
import colorsys

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


class Drawer:
    def __init__(self, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT):
        self.screen = turtle.Screen()
        self.screen.setup(width=screen_width, height=screen_height)
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.width(50)
        self.t.penup()
        self.t.setx(- self.screen.window_width() // 2)
        self.t.sety(self.screen.window_height() // 2)
        self.t.pendown()
        self.line_counter = 0

    def finish(self):
        turtle.done()

    def draw_syllable(self, onset_vals, nucleus_vals, coda_vals):
        hue = sum(nucleus_vals) / len(nucleus_vals)
        print(hue)
        if len(onset_vals) == 0 and len(coda_vals) == 0:
            color = colorsys.hsv_to_rgb(hue / 360, 1, 1)
            print(color)
            self.t.pencolor(color)
            self.t.forward(50)
        else:
            for p in onset_vals:
                sat = p[0]
                value = p[1]
                color = colorsys.hsv_to_rgb(hue / 360, sat / 100, value / 100)
                print(color)
                self.t.pencolor(color)
                self.t.forward(50)
            for p in coda_vals:
                sat = p[0]
                value = p[1]
                color = colorsys.hsv_to_rgb(hue / 360, sat / 100, value / 100)
                print(color)
                self.t.pencolor(color)
                self.t.forward(50)

    def draw_spacebar(self):
        self.t.pencolor("white")
        self.t.forward(50)

    def goto_next_line(self):
        self.line_counter += 1
        self.t.penup()
        self.t.setx(- self.screen.window_width() // 2)
        self.t.sety(self.screen.window_height() // 2 - 50 * self.line_counter)

import cairo
import math
import numpy as np

class Drawer:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.x = int(self.w / 2)
        self.y = int(self.h * 0.8)
        self.angle = 90

        self.heading = 0
        self.left = 0
        self.up = 0

        self.stack = []

        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
        self.cr = cairo.Context(self.surface)
        self.cr.rectangle(0, 0, w, h)
        self.cr.set_source_rgb(255, 255, 255)
        self.cr.set_line_width(1)
        self.cr.set_line_cap(cairo.LINE_CAP_BUTT)
        self.cr.fill()

    def goto(self, p):
        self.x = p[0]
        self.y = p[1]

    def rotate(self, p1, p2, t):
        x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sint, cost = math.sin(t), math.cos(t) 

        x3 = x1 + cost * dx + sint * dy
        y3 = y1 - sint * dx + cost * dy
        return (int(x3), int(y3))

    def rotate(self, angle):
        self.angle +=angle

    def forward(self, distance, draw=True):
        a = (self.angle * math.pi) / 180
        x2 = (self.x + math.cos(np.double(a))*distance)
        y2 = (self.y - math.sin(np.double(a))*distance)
        if(draw):
            self.cr.move_to(self.x, self.y)
            self.cr.line_to(x2, y2)
            self.cr.set_source_rgb(0, 0, 0)
            self.cr.set_line_cap(cairo.LINE_CAP_BUTT)
            self.cr.stroke()
        self.x, self.y = x2, y2

    def setangle(self, angle):
        self.angle = angle
    
    def addangle(self, angle):
        self.angle += angle 

    def save(self, name="image"):
        self.surface.write_to_png(name+".png")
        self.stack = []
        self.x = int(self.w / 2)
        self.y = int(self.h * 0.8)

    def push_state(self):
        self.stack.append((self.get_angle(), self.get_position()))
    
    def pop_state(self):
        heading, pos = self.stack.pop()
        self.goto(pos)
        self.setangle(heading)

    def get_position(self):
        return (self.x, self.y)
    
    def get_angle(self):
        return self.angle

    def left(self, angle):
        self.addangle(angle)
    
    def right(self, angle):
        self.addangle(-angle)

def test():

    d = Drawer(500,500)
    d.goto((250, 250))
    d.up(100)
    d.right(45)
    d.up(50)
    d.left(45)
    d.left(45)
    d.up(50)
    d.save()

#test()

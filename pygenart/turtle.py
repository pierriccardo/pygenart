import cairo
import math
import numpy as np

class Turtle:

    def __init__(self, canvas):
        self.canvas = canvas
        self.w = canvas.w
        self.h = canvas.h
        self.x = int(self.w / 2)
        self.y = int(self.h * 0.8)

        self.angle = 90
        self.stack = []

    def goto(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, x1, y1, x2, y2, t):
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
        if draw:
            self.canvas.line(self.x, self.y, x2, y2, color=[0,0,0,1])
        self.x, self.y = x2, y2

    def setangle(self, angle):
        self.angle = angle
    
    def addangle(self, angle):
        self.angle += angle 

    def push_state(self):
        self.stack.append((self.get_angle(), self.get_position()))
    
    def pop_state(self):
        heading, pos = self.stack.pop()
        self.goto(pos[0], pos[1])
        self.setangle(heading)

    def get_position(self):
        return (self.x, self.y)
    
    def get_angle(self):
        return self.angle

    def left(self, angle):
        self.addangle(angle)
    
    def right(self, angle):
        self.addangle(-angle)


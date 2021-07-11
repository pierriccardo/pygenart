from sketches.sketch import Sketch
from pygenart.turtle import Turtle
import numpy as np 

class TurtleTestSketch(Sketch):

    def __init__(self, canvas):
        super().__init__(canvas)
        turtle = Turtle(canvas)
        self.turtle = turtle
        

    def draw(self):
        self.turtle.forward(1.0)
        self.turtle.rotate(4.5)
        self.c.line(0,0,100,100, color=[0,0,0,1])
        self.turtle.forward(10 * np.random.random())
        self.turtle.rotate(4.5)
        self.turtle.forward(1.0 * np.random.random())
        self.turtle.rotate(4.5)
        self.turtle.forward(10 * np.random.random())
        self.turtle.rotate(4.5)
        self.turtle.forward(10 * np.random.random())
        self.turtle.rotate(4.5)
        self.turtle.forward(1.0 * np.random.random())
        
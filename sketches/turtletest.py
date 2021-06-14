from sketches.sketch import Sketch
import numpy as np 

class TurtleTestSketch(Sketch):

    def __init__(self, canvas, turtle):
        super().__init__(canvas)
        self.turtle = turtle

    def draw(self):
        self.c.background(255, 255, 255,1)
        self.turtle.forward(10)
        self.turtle.rotate(45)
        self.turtle.forward(10 * np.random.random())
        self.turtle.rotate(45)
        self.turtle.forward(10 * np.random.random())
        self.turtle.rotate(45)
        self.turtle.forward(10 * np.random.random())
        self.turtle.rotate(45)
        self.turtle.forward(10 * np.random.random())
        self.turtle.rotate(45)
        self.turtle.forward(10 * np.random.random())
        
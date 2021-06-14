from sketches.sketch import Sketch
from tqdm import tqdm
import numpy as np
from numpy import random

class Walker:
    def __init__(self):
        self.x = random.random()
        self.y = random.random()
        self.color = [random.random(), random.random(), random.random(), 1]


class RandomWalksSketch(Sketch):

    def __init__(self, canvas):
        super().__init__(canvas)

    def draw(self):

        steps = 10000
        walkers = []
        for x in range(1):
            walkers.append(Walker())

        self.c.background(0,0,0,1)

        x_unit, y_unit = 10/self.c.w, 10/self.c.h

        for s in tqdm(range(steps)):
            for w in walkers:
            
                choice = np.random.choice([1,2,3,4])

                wx2, wy2 = w.x, w.y
                if choice == 1:
                    wx2 += x_unit
                if choice == 2: 
                    wx2 -= x_unit
                if choice == 3: 
                    wy2 += y_unit
                if choice == 4: 
                    wy2 -= y_unit

                self.c.line(w.x, w.y, wx2, wy2, color=w.color, line_width=0.001)
                w.x, w.y = wx2, wy2

        return self.c






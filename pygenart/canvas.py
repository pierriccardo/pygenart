from random import random
import time
import cairo
import logging
import os
import math
from time import strftime, gmtime

import numpy as np

class Canvas():

    def __init__(self, w, h, seed, format="png", savepath="./", name="img"):
        self.w = w # width 
        self.h = h # height
        self.format = format # png or svg
        self.savepath = savepath # path to save the image

        timestamp = strftime("%d-%m-%Y-%H-%M-%S", gmtime())
        self.filename = os.path.join(savepath, f'{name}-{seed}-{timestamp}.{format}')
        self.latestfn = os.path.join(savepath, f'latest.{format}')

        self.context = self.setup()
        

    def setup(self):
        if self.format == "png":
            self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.w, self.h)
            
        elif self.format == "svg":
            self.surface = cairo.SVGSurface(self.filename, self.w, self.h)

        else:
            logging.error("invalid format: choose png or svg")
            return 0
        
        ctx = cairo.Context(self.surface)
        ctx.scale(self.w, self.h) 

        ctx.rectangle(0, 0, self.w, self.h)  # Rectangle(x0, y0, x1, y1)

        pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
        pat.add_color_stop_rgba(1, 0.7, 0, 0, 0.5)  # First stop, 50% opacity
        pat.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1)  # Last stop, 100% opacity
        ctx.set_source(pat)
        ctx.fill()       
        return ctx
    
    def export(self):
        if self.format == "png":
            self.surface.write_to_png(self.filename)
            self.surface.write_to_png(self.latestfn)

        elif self.format == "svg":
            self.surface.finish()

        else: 
            logging.error("invalid format: choose png or svg")

        logging.info(f'img saved in: {self.filename}') 

    def line(self, x1, y1, x2, y2, color=[0,0,0,1], line_width=0.01, line_cap=cairo.LINE_CAP_SQUARE):
        # line_cap :
        # cairo.LINE_CAP_SQUARE
        # cairo.LINE_CAP_BUTT
        # cairo.LINE_CAP_ROUND

        r,g,b,a = color
        self.context.set_source_rgba(r,g,b,a)
        self.context.set_line_width(line_width)
        self.context.set_line_cap(line_cap)
        self.context.move_to(x1, y1)
        self.context.line_to(x2, y2)
        self.context.stroke()

        logging.info(f'line from point {x1, y1}')
        logging.info(f'line to   point {x2, y2}')
    
    def arc(self, cx, cy, radius, start_angle, stop_angle, color=[0,0,0,1]):
        r,g,b,a = color
        self.context.set_source_rgba(r,g,b,a)

        self.context.move_to(cx, cy)
        self.context.arc(cx, cy, radius, start_angle, stop_angle)
        #self.context.stroke()
        

    def rectangle(self,x1, y1, x2, y2, line_width=0.01):
        # TODO: fix this
        self.context.rectangle(x1, y1, x2, y2)
        pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
        pat.add_color_stop_rgba(random(), random(), random(), random(), 1)  # Last stop, 100% opacity
        self.context.set_source(pat)
        self.context.fill()     

        logging.info(f'rect from point {x1, y1} to w, h = {x2, y2}')
        logging.info(f'line to   point x2, y2 is {x2, y2}')
        
    def background(self, r, g, b, a):
        self.context.set_source_rgba(r, g, b, a)
        self.context.paint()

    def scale_points(self, x, y):
        return x / self.w, y / self.h

        
from os import name, path
from pygenart.turtle import Turtle
import numpy as np
from numpy import random
import math
import configparser
import argparse
import logging
from tqdm import tqdm



#------------------------------
# ARG PARSER
#------------------------------
parser = argparse.ArgumentParser(description='Parameters shortcut for generative art')
parser.add_argument('--seed',     '-s',  type=int,  default=0,       help='random seed')
parser.add_argument('--width',    '-W',  type=int,  default=1000,    help='specify width of the image')
parser.add_argument('--height',   '-H',  type=int,  default=1000,    help='specify height of the image')
parser.add_argument('--format',   '-f',  type=str,  default='png',   help='specify format of the image')
parser.add_argument('--savepath', '-sp', type=str,  default='./img', help='specify savepath of the image')
parser.add_argument('--name',     '-n',  type=str,  default='img',   help='specify savepath of the image')
parser.add_argument('--log',      '-l',  type=int,  default=40,      help='set log level')
parser.add_argument('--logfile', '-lf',  type=bool, default=False,   help='true to output log in a file')
parser.add_argument('--sketch',  '-sk',  type=int,  default=0,       help='select the sketch')
args = parser.parse_args()

#------------------------------
# CONFIG SETUP
#------------------------------
config = configparser.ConfigParser()
config.read('config.ini')

# TODO: add colors configs

#------------------------------
# LOGGER SETUP
#------------------------------
lvl = logging.getLevelName(args.log)

if args.logfile:
    path_logfile = config['DEFAULT']['path_logfile']
    logging.basicConfig(filename=path_logfile, level=lvl)#args.log)
else:
    logging.basicConfig(level=lvl)
logging.info('Started')

        
#------------------------------
# LOAD PARAMS
#------------------------------
WIDTH       = args.width  
HEIGHT      = args.height 
SEED        = args.seed   
FORMAT      = args.format
SAVEPATH    = args.savepath 
NAME        = args.name 

#------------------------------
# TOOLS SETUP
#------------------------------
from pygenart.canvas import Canvas
from pygenart.turtle import Turtle

c = Canvas(WIDTH, HEIGHT, SEED, format=FORMAT, savepath=SAVEPATH, name=NAME)
turtle = Turtle(c)
np.random.seed(SEED)
#------------------------------
# SKETCH SELECTION 
#------------------------------
from sketches.randomwalks import RandomWalksSketch
from sketches.turtletest import TurtleTestSketch

sketch = None

if args.sketch == 1:
    sketch = RandomWalksSketch(c)
elif args.sketch == 2:
    sketch = TurtleTestSketch(c, turtle)
else:
    logging.error("main: the sketch selected doesn't exist")

            
def main():
    sketch.draw()
    c.export()

if __name__ == "__main__":
    main()



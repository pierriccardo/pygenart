import matplotlib 
import random
from drawer import Drawer
from symbols import *
from grammars import *
import yaml
import argparse



def main(grammar):
    w, h = 1000, 1000
    drawer = Drawer(w, h)
    drawer.goto((500 , h-200))

    stream = open(grammar, "r")
    dictionary = yaml.load(stream)
    
    segment = dictionary['SEGMENT']
    iterations = dictionary['ITERATIONS']
    angle = dictionary['ANGLE']
    axiom = dictionary['AXIOM']
    rules = []
    for r in dictionary['RULES']:
        rule = r.split()
        rule.remove('->')
        rules.append(rule)


    s = run(rules, iterations, axiom)
    name = "angle-" + str(angle) + "iters-" + str(iterations) + "-axiom" + axiom
    draw(drawer, s, angle, segment, "imgs/" + name)

def apply_rules(c, rules):
    for r in rules:
        if c == r[0]: return r[1]
    return c

def derivations(string, rules):
    newstring = ""
    for c in string:
        newstring += apply_rules(c, rules)
    return newstring

def run(rules, iterations, string):
    for i in range(0, iterations):
        string = derivations(string, rules)
    return string

def draw(drawer, string, angle, segment, name="image"):
    stack = []
    for s in string:
        symbol(s, drawer, segment, angle)
    drawer.save(name)
    drawer.save('last')

main("grammars/1.yaml")

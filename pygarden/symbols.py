
def symbol(c, drawer, distance=5, angle=45):
    if   c == 'F': drawer.forward(distance)
    elif c == 'f': drawer.forward(distance, False)
    elif c == '0': drawer.forward(distance)
    elif c == '[': drawer.push_state()
    elif c == ']': drawer.pop_state() 
    elif c == '+': drawer.right(angle)
    elif c == '-': drawer.left(angle)
    
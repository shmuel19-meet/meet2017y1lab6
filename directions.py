UP_ARROW="up"
LEFT_ARROW="left"
RIGHT_ARROW="right"
DOWN_ARROW="down"
SPACEBAR="space"
UP=0
LEFT=1
RIGHT=2
DOWN=3
direction=UP

def up():
    global direction
    direction=UP
    print("you pressed up")
    
def left():
    global direction
    direction=LEFT
    print("you pressed left")
    
def right():
    global direction
    direction=RIGHT
    print("you pressed right")

def down():
    global direction
    direction=DOWN
    print("you pressed down")

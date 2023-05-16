from graphics import *
import math
import time

win = GraphWin("Question 2&3")
win.setCoords(0,0,120,120)

c = Circle(Point(60,100),5)
c.draw(win)
c.setOutline("red")
c.setFill("yellow")

line = Line(Point(30,10),Point(90,10))
line.draw(win)

h_line = 10
h = 100 - h_line
g = 9.8
dt = 0.1
v1 = 0.0

while True:
    while True:
        time.sleep(0.1)
        v2 = v1 + g * dt
        dh = (v2 + v1)/2 * dt
        v1 = v2
        
        c.move(0, -dh)

        if c.getCenter().getY() - 5 < 10:
            break

    v1 = v1 * 0.8
    
    if v1 < 0.001:
        break

    while True:
        time.sleep(0.1)
        v2 = v1 - g * dt
        dh = (v2 + v1)/2 * dt
        v1 = v2

        c.move(0, dh)

        if v1 <= 0:
            break




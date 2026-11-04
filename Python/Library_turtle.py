import turtle
import math
from math import sqrt

t = turtle.Turtle()

t.color("red")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.color("blue")
t.begin_fill()
t.goto(50, 0)
t.left(45)
for _ in range(4):
    t.forward(50*sqrt(2))
    t.left(90)

t.end_fill()

t.left(-45)
t.goto(-200, 0)
t.color("green")
for _ in range(3):
    t.forward(100)
    t.left(120)

turtle.done()
    

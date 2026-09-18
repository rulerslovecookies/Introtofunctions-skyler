import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
def addSquares(iRange):
    length = 25
    def square(length, angle):
        for i in range(4):
            t.forward(length)
            t.left(angle)
    for i in range(iRange):
        square(length, 90)
        length += 25
addSquares(5)
turtle.done()
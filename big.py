import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(1000001)
def square(length, angle):
        for i in range(4):
            t.forward(length)
            t.left(angle)
length=5
for i in range(60):
        print (i)
        square(length, 90)
        t.right(5)
        length+=5
turtle.done()
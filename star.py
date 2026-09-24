import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(10000000)
def square(length, angle):
        for i in range(5):
            t.forward(length)
            t.left(angle)
length=5
for i in range(70):
        
        print (i)
        square(length, 144)
        t.right(5)
        length+=5
turtle.done()
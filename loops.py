import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
for i in range(60):
    def square(X):
        for i in range(4):
            t.forward(X)
            t.left(90)
    square(100)
    t.right(5)
    print (i)
turtle.done()
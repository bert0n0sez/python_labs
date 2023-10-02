import turtle
import numpy as np
turtle.shape('turtle')
turtle.right(90)

def k(n):
    while n<10**1000:
        turtle.forward(n)
        turtle.left(90)
        n +=10 
k(10)






import turtle 
import numpy as np

turtle.shape('turtle')
turtle.speed(0)

def krug():

    for i in range(360):
        turtle.forward(1)
        turtle.right(1)

def zvetok():
    for i in range(6):
        krug()
        turtle.right(60)


zvetok()
turtle.mainloop()

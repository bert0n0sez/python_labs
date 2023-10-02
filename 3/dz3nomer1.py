from random import *
import turtle
turtle.shape('turtle')
turtle.speed(0)
def b():
    for i in range( 10 ** 10):
        x=random()
        if x>=0.5: turtle.forward(randint(0, 100))
        else: turtle.backward(randint (0,100))
        y=random()
        if y>=0.5: turtle.right(randint (0, 360))
        else: turtle.left(randint(0,360))
b()
        

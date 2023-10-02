import turtle 
turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)
def poly():
    for i in range(180):
        turtle.forward(1)
        turtle.right(1)

def mini():
    for i in range(90):
        turtle.forward(0.3)
        turtle.right(2)

def gr():
    for i in range(100):
        poly()
        mini()

gr()

turtle.mainloop()
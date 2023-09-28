import turtle 
turtle.shape('turtle')
turtle.speed(0)

def krug(r):

    for i in range(360):
        turtle.forward(r)
        turtle.right(1)


def ba():
    r=1

    for i in range(10):
        krug(r)
        turtle.right(180)
        krug(r)
        r +=1

ba()

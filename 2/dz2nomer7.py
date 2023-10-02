import turtle
turtle.shape('turtle')
def sprl():
    n = 15
    m = 1
    for _ in range(10**10): 
        turtle.forward(m)
        turtle.right(n)
        m += 1  

sprl()

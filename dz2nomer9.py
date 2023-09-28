import turtle 
import numpy as np
turtle.shape('turtle')




def pov(n, r, k):
    
    dlina = 2 * r * np.sin( np.pi / n)
    ygol = 360 / n
    for i in range( n - 1 ):
        turtle.forward( dlina )
        turtle.right( ygol )
    turtle.forward( dlina )
    turtle.penup()
    turtle.forward( k )
    turtle.pendown()
    turtle.right( ygol )




def nangle():
    
    k= 10
    n = 3
    r = 10

    dlina = 2 * r * np.sin( np.pi / n)
    ygol = 360 / n

    for i in range(7):
        pov(n, r, k )
        n +=1
        r *=2
        k *=1.5
    
        
        
nangle()


    

  
import turtle

x = 0
y = 0
Vx = 0.7
Vy = 2
ay = -0.1 
dt = 0.1 

t = turtle.Turtle()
turtle.tracer(0, 0)

while True:
    x += Vx * dt
    y += Vy * dt + ay * dt**2 / 2
    Vy += ay * dt

    if y <= 0:
        Vy = -Vy * 0.8

    
    t.goto(x, y)

  
    turtle.update()

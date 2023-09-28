import turtle 
turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)

def krug():
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.circle(200)


def mini(x, y):
    turtle.penup()
    turtle.goto(x, -y)
    turtle.pendown()
    turtle.circle(20)

turtle.begin_fill()
turtle.color('yellow')
krug()
turtle.end_fill()


turtle.begin_fill()
turtle.color('red')
mini(-250, 100)
turtle.end_fill()

turtle.begin_fill()
turtle.color('red')
mini(-110, 100)
turtle.end_fill()

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.right(180)
turtle.width(10)
turtle.forward(50)


def polykrug():
    turtle.penup()
    turtle.goto(-250, -300)
    turtle.pendown()
    turtle.circle(50, 180)


polykrug()


turtle.mainloop()
import turtle
turtle.shape('turtle')


def star(n):
    ygol = 180 - (180 / n)
    for i in range(n):
        turtle.forward(100)
        turtle.right(ygol)


n = int(input())


star(n)


turtle.done()

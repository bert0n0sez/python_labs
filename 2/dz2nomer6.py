import turtle

turtle.shape('turtle')

m=int(input())
n=360//m

def spider_leg(m):
    turtle.forward(100)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(100)
    turtle.right(180-m)

for i in range(n):
    spider_leg(n)


from random import randint
import turtle

number_of_turtles = 10
steps_of_time_number = 1000
screen_size = 500
collision_radius = 20

wn = turtle.Screen()
wn.setup(screen_size, screen_size)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))

for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(2)  

        
        if unit.xcor() > screen_size / 2 or unit.xcor() < -screen_size / 2:
            unit.setheading(unit.heading() + 180)

        if unit.ycor() > screen_size / 2 or unit.ycor() < -screen_size / 2:
            unit.setheading(unit.heading() + 180)

        for other_unit in pool:
            if other_unit != unit and unit.distance(other_unit) < collision_radius:
                unit.setheading(unit.heading() + 180)  
                other_unit.setheading(other_unit.heading() + 180)


turtle.done()

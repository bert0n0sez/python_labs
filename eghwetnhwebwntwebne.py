import turtle

# Функция для рисования правильного n-угольника
def draw_polygon(t, n, length):
    angle = 360 / n
    for _ in range(n):
        t.forward(length)
        t.right(angle)

# Функция для рисования 10 вложенных многоугольников
def draw_nested_polygons():
    wn = turtle.Screen()
    wn.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)

    # Радиус описанной окружности для правильного n-угольника
    def calculate_radius(n, length):
        import math
        angle = math.radians(360 / n)
        return length / (2 * math.sin(angle / 2))

    # Рисуем 10 вложенных многоугольников
    for i in range(10):
        n = i + 3  # число сторон многоугольника: от 3 до 12
        length = 50 * (i + 1)  # длина стороны многоугольника увеличивается с каждой итерацией
        radius = calculate_radius(n, length)  # находим радиус описанной окружности
        t.penup()
        t.goto(-radius, -radius)
        t.pendown()
        draw_polygon(t, n, length)

    wn.exitonclick()

# Вызываем функцию для рисования 10 вложенных многоугольников
draw_nested_polygons()

import matplotlib.pyplot as plt

with plt.xkcd():
    function = input("Введите функцию: ")
    x = []
    y = []
    for i in range(-10, 11):
        x.append(i)
        y.append(eval(function, {'x': i}))

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции: {}'.format(function))
    plt.show()
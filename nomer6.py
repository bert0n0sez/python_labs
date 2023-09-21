import numpy as np
import matplotlib.pyplot as plt

def func(x, a, b, N):
    result = 0
    for n in range(N+1):
        result += b**n * np.cos(a**n * np.pi * x)
    return result

b = 0.5
a = 3
N = 10
x = np.linspace(-10, 10, 1000)
y = func(x, a, b, N)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции Вейерштрасса')
plt.show()

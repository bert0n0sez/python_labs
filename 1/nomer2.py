import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x*x - x - 6
x = np.linspace(-10, 10, 100) 
y = f(x) 
plt.plot(x, y)
roots = np.roots([1, -1, -6])
plt.scatter(roots, np.zeros_like(roots), color='red') 
plt.show()
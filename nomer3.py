import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.log(((x**2 + 1)*np.exp(- np.abs(x)/10)) )/np.log(1+np.tan(1/1+np.sin(x)*np.sin(x)))
x = np.linspace(-10, 10, 100) 
y = f(x) 
plt.plot(x, y)
plt.show()
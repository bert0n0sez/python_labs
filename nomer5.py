import numpy as np
import matplotlib.pyplot as plt

x = [1, 10, 1000]
y = [-1.7317613767816733, -0.43518957096234573, -0.04491576055082721]
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.grid()
plt.show()
"""
Application: Least squares fit to noisy data
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.linspace(0, 10, 20)
y = 2*x + 1 + np.random.normal(0, 2, size=x.shape)
A = np.vstack([x, np.ones_like(x)]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
plt.plot(x, y, 'o', label='Data')
plt.plot(x, m*x + c, label='Fit')
plt.legend()
plt.show()

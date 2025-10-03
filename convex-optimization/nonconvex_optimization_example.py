"""
Nonconvex optimization: minimize f(x) = x^4 - 3x^3 + 2
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 - 3*x**3 + 2

def df(x):
    return 4*x**3 - 9*x**2

def gradient_descent(x0, lr=0.01, tol=1e-6, max_iter=1000):
    x = x0
    for i in range(max_iter):
        x_new = x - lr*df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

x = np.linspace(-1, 3, 200)
y = f(x)
plt.plot(x, y, label='f(x)')
min_x = gradient_descent(0.0)
plt.plot(min_x, f(min_x), 'ro', label='Minimum')
plt.legend()
plt.title('Nonconvex Optimization')
plt.show()

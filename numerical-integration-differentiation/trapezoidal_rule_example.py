"""
Trapezoidal rule for integrating f(x) = x^2 on [0, 1]
"""
import numpy as np

def f(x):
    return x**2

a, b, n = 0, 1, 10
x = np.linspace(a, b, n+1)
y = f(x)
I = np.trapz(y, x)
print(f"Approximate integral: {I}")

"""
Lagrange interpolation for three points
"""
import numpy as np
import matplotlib.pyplot as plt

def lagrange_basis(x, i, x_points):
    basis = 1
    for j, xj in enumerate(x_points):
        if i != j:
            basis *= (x - xj) / (x_points[i] - xj)
    return basis

def lagrange_interpolation(x, x_points, y_points):
    return sum(y_points[i] * lagrange_basis(x, i, x_points) for i in range(len(x_points)))

x_points = np.array([0, 1, 2])
y_points = np.array([1, 3, 2])
x = np.linspace(0, 2, 100)
y = [lagrange_interpolation(xi, x_points, y_points) for xi in x]

plt.plot(x_points, y_points, 'o', label='Points')
plt.plot(x, y, label='Lagrange Interpolation')
plt.legend()
plt.show()

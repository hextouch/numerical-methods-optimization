"""
Conjugate gradient method for solving Ax = b
"""
import numpy as np

A = np.array([[4, 1], [1, 3]])
b = np.array([1, 2])
x = np.zeros_like(b)
r = b - A @ x
p = r.copy()
for i in range(2):
    Ap = A @ p
    alpha = r @ r / (p @ Ap)
    x = x + alpha * p
    r_new = r - alpha * Ap
    beta = r_new @ r_new / (r @ r)
    p = r_new + beta * p
    r = r_new
print(f"Solution x: {x}")

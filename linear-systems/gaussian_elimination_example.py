"""
Gaussian elimination for solving Ax = b
"""
import numpy as np

A = np.array([[2, 1], [1, 3]])
b = np.array([1, 2])
x = np.linalg.solve(A, b)
print(f"Solution x: {x}")

"""
Power method for dominant eigenvalue of a matrix
"""
import numpy as np

A = np.array([[2, 1], [1, 3]])
x = np.random.rand(2)
for _ in range(10):
    x = A @ x
    x = x / np.linalg.norm(x)
lambda_ = (A @ x)[0] / x[0]
print(f"Dominant eigenvalue: {lambda_}")

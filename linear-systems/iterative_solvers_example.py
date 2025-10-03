"""
Iterative solvers: Jacobi and Gauss-Seidel methods for Ax = b
"""
import numpy as np

def jacobi(A, b, x0, tol=1e-6, max_iter=100):
    x = x0.copy()
    D = np.diag(A)
    R = A - np.diagflat(D)
    for _ in range(max_iter):
        x_new = (b - np.dot(R, x)) / D
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    return x

def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    x = x0.copy()
    n = len(b)
    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    return x

if __name__ == "__main__":
    A = np.array([[4, 1], [2, 3]], dtype=float)
    b = np.array([1, 2], dtype=float)
    x0 = np.zeros_like(b)
    print("Jacobi:", jacobi(A, b, x0))
    print("Gauss-Seidel:", gauss_seidel(A, b, x0))

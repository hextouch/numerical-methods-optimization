"""
Duality and Lagrange multipliers: minimize f(x) = x^2 subject to x >= 1
"""
import numpy as np

def f(x):
    return x**2

def lagrangian(x, lam):
    return f(x) + lam * (1 - x)

# Analytical solution
lam = 0
x = 1
if lam >= 0 and x >= 1:
    print(f"Optimal x: {x}, Lagrange multiplier: {lam}")
else:
    print("No feasible solution found analytically.")

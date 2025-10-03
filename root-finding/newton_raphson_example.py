"""
Newton-Raphson method for finding roots of f(x) = x^2 - 2
"""
def f(x):
    return x**2 - 2

def df(x):
    return 2*x

def newton_raphson(x0, tol=1e-6, max_iter=20):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

if __name__ == "__main__":
    root = newton_raphson(1.0)
    print(f"Root: {root}")

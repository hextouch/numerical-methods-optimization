"""
Unconstrained optimization: minimize f(x) = (x-2)^2
"""
def f(x):
    return (x-2)**2

def df(x):
    return 2*(x-2)

def gradient_descent(x0, lr=0.1, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - lr*df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

if __name__ == "__main__":
    min_x = gradient_descent(0.0)
    print(f"Minimum at x = {min_x}")

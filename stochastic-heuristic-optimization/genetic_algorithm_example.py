"""
Simple genetic algorithm for maximizing f(x) = x*sin(x)
"""
import numpy as np

np.random.seed(0)
def f(x):
    return x * np.sin(x)

pop = np.random.uniform(0, 10, 20)
for generation in range(10):
    fitness = f(pop)
    parents = pop[np.argsort(fitness)[-10:]]
    children = parents + np.random.normal(0, 0.1, 10)
    pop = np.concatenate([parents, children])
    pop = np.clip(pop, 0, 10)
best = pop[np.argmax(f(pop))]
print(f"Best solution: x = {best}")

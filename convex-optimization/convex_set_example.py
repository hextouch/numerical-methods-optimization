"""
Visualizing a convex set in 2D
"""
import numpy as np
import matplotlib.pyplot as plt

points = np.random.rand(30, 2)
from scipy.spatial import ConvexHull
hull = ConvexHull(points)
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.title('Convex Hull (Convex Set)')
plt.show()

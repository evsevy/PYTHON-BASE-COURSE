import numpy as np

#define left-hand side of equation
left_side = np.array([[6, 2, 2, 1], [2, 1, 1, 0], [3, 2, 2, 4], [2, 0, 5, 5]])

#define right-hand side of equation
right_side = np.array([37, 14, 28, 28])

#solve for w, x, y, and z
print(np.linalg.inv (left_side). dot (right_side))


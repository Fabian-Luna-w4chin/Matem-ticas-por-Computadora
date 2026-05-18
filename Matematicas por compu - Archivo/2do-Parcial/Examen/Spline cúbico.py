import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([0.0, 0.1, 0.25, 0.5, 0.75, 1.0, 1.41, 2.12, 2.83, 4.0, 5.0])
y = np.array([0.0000, 0.4292, 2.1162, 5.6133, 8.3122, 9.9700, 10.4153, 10.0860, 9.9827, 10.0004, 10.0001])

cs = CubicSpline(x, y, bc_type='natural')

x_new = np.linspace(0.0, 0.1)
y_new = cs(x_new)

print(y_new)

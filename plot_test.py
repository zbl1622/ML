import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-100, 100, 400, endpoint=True)
y = 0.1 * x * x * x * x - 2 * x * x * x - 10 * x * x + 1 * x - 2

plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 400, endpoint=True)
y = 0.75 * x * x * x * x - 0 * x * x * x - 2.75 * x * x - 0 * x + 1

plt.plot(x, y)
plt.show()

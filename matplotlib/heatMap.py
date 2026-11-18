import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

plt.imshow(data,cmap="coolwarm")
plt.colorbar()

plt.title("Heat map")
plt.xlabel("Column")
plt.ylabel("Rows")
plt.show()
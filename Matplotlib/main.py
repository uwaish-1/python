import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([7, 23, 38, 5])



line_style = dict(marker = ".",
               markersize = 20,
               linestyle ="solid",
               linewidth=2,
               color="#4582de")

plt.plot(x, y1, **line_style)
plt.plot(x, y2, **line_style)
plt.show()

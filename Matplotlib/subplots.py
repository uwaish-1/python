import matplotlib.pyplot as plt
import numpy as np

# Figure = The entire canva
# Ax = A single plot (subplot)

x = np.array([1, 2, 3, 4, 5])
figure, axes = plt.subplots(2,2)
axes[0,0].plot(x, x*2, color ="red")
axes[0,0].set_title("x*2")

plt.tight_layout()
plt.show()

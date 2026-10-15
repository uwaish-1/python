import matplotlib.pyplot as plt
import numpy as np


# Scatter graph = shows the relationship between two variables
#                 helps to identify a correlation(+, -, None)
#                 example: study hours vs test scores
 
x = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8])
y = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87])

plt.scatter(x, y, color="skyblue",
                  alpha = 0.1,
                  s = 200)

plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grades")
plt.show()
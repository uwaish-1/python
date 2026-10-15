import matplotlib.pyplot as plt
import numpy as np

#  Histogram = A visual represntation of the distribution of quantitative data.
            #  They group values into bins(intervals)
            #  and counts how many fall in each range

scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100)

plt.title("Test Scores")
plt.xlabel("Score")
plt.ylabel("# of Students")
plt.hist(scores, bins=10)
plt.show()
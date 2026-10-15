import matplotlib.pyplot as plt
import numpy as np

# pie chart = Circular chart divided into slices to show percentages of the total.
            #  Good for visualizing distribution among categories

categories = ["Freshman", "Sophomores", "Juniors", "Seniors"]
values = [300, 250, 275, 225]
colors = ["red","yellos","blue","green"]

plt.pie(values, labels= categories,
                autocpt ="%1.1f%%",
                colors = colors,
                explode=[0,0,0,0.1],
                shadow=True,
                startangle=90)

plt.title("College")

plt.show()
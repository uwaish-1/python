import matplotlib.pyplot as plt
import numpy as np

# Bar chart = compare categories of data by representing each category with a bar

categories = np.array(["Greains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4, 3, 2, 5, 3, 1])

plt.bar(categories, values, color ="skyblue")
plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")


# plt.barh(categories, values, color ="skyblue")
plt.show()

import pandas as pd

# print(pd.__version__)

# Series = A pandas 1-dimensional labeled array that can hold any data type
           # think of it like a single column in a spreadsheet (1-Dimensional)

# data = [100, 102, 104]

# series = pd.Series(data, index =["apartment #1", "apartment #2", "apartment #3"])
# print(series)
# print(series.loc["apartment #1"])

# key-error
# print(series.loc["apartment #4"])

# series.loc["apartment #3"] = 200
# print(series)
# or
# print(series.iloc[2])


# data = [100, 102, 104, 200, 202]
# series = pd.Series(data, index = ["a", "b", "c", "d", "e"])
# print(series[series >= 200])


# calories = {"Day 1": 1750, "Day 2": 2100,
#             "Day3" : 1700}
# series = pd.Series(calories)
# print(series)
# print(series.loc["Day 1"])


import pandas as pd

df = pd.read_csv("data.csv")

#  Whole dataframe
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())


# Single column
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())

#  Creating gropu by object
# group = df.groupby("Type1")
# print(group["Height"].mean())
import pandas as pd

# Dataframe = A tabular data structure with rows and columns. (2 Dimensional)
            # Similar to an excel spreadsheet

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age" : [30, 35, 50]
}

df = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3"])
print(df)
print(df.loc["Employee 1"])
print(df.iloc[1])
print(df.iloc[2])

#  Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]
print(df)

# Add a new row
new_row = pd.DataFrame([{"Name": "Sandy", "Age":28, "Job": "Engineer"}],
                        index=["Employee 4"])
df = pd.concat([df, new_row])
print(df)

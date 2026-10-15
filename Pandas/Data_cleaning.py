import pandas as pd

# Data Cleaning = the process of fixing/removing:
#                 incomplete, incorrect, or irrevelant data.
#                  75% of work done with Pandas is data cleaning

df = pd.read_csv("data.csv")
# print(df)

# 1. Drop irrevelant columns
df = df.drop(columns=["Legendary"])
print(df)

# df = df.drop(columns=["Legendary","No"])

# 2. Handle missing data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2": "None"})

print(df.to_string())

# 3. Fix inconsistent value

df["Type1"] = df["Type1"].replace({"Grass": "GRASS"})



# 4. Standardize Text
df["Name"] = df["Name"].str.lower()
print(df.to_string())

# 5. Fix data types
df["legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicate files
df = df.drop_duplicates()
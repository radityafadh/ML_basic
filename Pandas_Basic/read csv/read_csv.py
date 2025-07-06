import pandas as pd

df = pd.read_csv("example.csv")
print(df)

#statistial descriptive
print(df.describe())
print(df.info())
print(df.head())
print(df.tail())
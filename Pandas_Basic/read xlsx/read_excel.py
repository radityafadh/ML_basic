import pandas as pd

df = pd.read_excel("example.xlsx", sheet_name="Sheet1")
print(df)

#statistial descriptive
print(df.describe())
print(df.info())
print(df.head())
print(df.tail())
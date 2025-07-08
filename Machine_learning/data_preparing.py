import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# import
df = pd.read_csv('personality_dataset.csv')
print(df.head())
print(df.info())

#encode the dataset
for column in df.columns:
    df[column] = pd.Categorical(df[column]).codes
print(df.head())
print(df.info())

#clean the dataset and remove outlier using z-score
df = df.dropna()
z_scores = np.abs((df - df.mean()) / df.std())
df = df[(z_scores < 3).all(axis=1)]
print(df.head())
print(df.info())
sns.boxenplot(data=df)
plt.show()

#histogram of each label comparing label 1 and 0
for column in df.columns:
    if column != "Personality":
        plt.hist(df[df["Personality"]==1][column], alpha=0.5, color="red", label="Introvert")
        plt.hist(df[df["Personality"]==0][column], alpha=0.5, color="green", label="Extrovert")   
        plt.title(f"{column} distribution")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.legend()
        plt.grid(True)
        plt.show()

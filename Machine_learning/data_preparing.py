import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# import
df = pd.read_csv('personality_dataset.csv')
print(df.head())
print(df.info())

# Binary encoding for "Yes"/"No" columns
binary_map = {"Yes": 1, "No": 0}
df["Stage_fear"] = df["Stage_fear"].map(binary_map)
df["Drained_after_socializing"] = df["Drained_after_socializing"].map(binary_map)

# Target encoding (Personality: Introvert=1, Extrovert=0)
df["Personality"] = df["Personality"].map({"Introvert": 1, "Extrovert": 0})

scaler = StandardScaler()
numerical_cols = ["Time_spent_Alone", "Social_event_attendance", 
                  "Going_outside", "Friends_circle_size", "Post_frequency"]
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Verify
print(df.head())
print(df.info())

#clean the dataset missing value and remove outlier using IQR
df = df.dropna()
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

for col in numerical_cols:
    df[col] = df[col].clip(lower_bound[col], upper_bound[col])
print(df.head())
print(df.info())
sns.boxenplot(data=df)
plt.show()

#check for imbalance and handle
sns.countplot(data=df, x="Personality")
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


#corralation analysis using seaborn heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5, square=True)
plt.show()

#split data train test 60 40 and the validation
def get_processed_datasets():
    # Split
    X = df.drop(columns=['Personality'])
    y = df['Personality']

    X_temp, X_test, y_temp, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    X_train, X_valid, y_train, y_valid = train_test_split(
        X_temp, y_temp, test_size=0.25, stratify=y_temp, random_state=42
    )

    # Normalize
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_valid_scaled = scaler.transform(X_valid)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_valid_scaled, X_test_scaled, y_train, y_valid, y_test
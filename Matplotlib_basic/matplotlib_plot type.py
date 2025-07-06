import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Line Plot
x = np.arange(0, 10, 0.1)
y = np.sin(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, color="red", label="sin(x)", linewidth=2, linestyle="--")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Matplotlib 1 - Line Plot")
plt.grid(True)
plt.legend()
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 5))
plt.scatter(x, y, color="red", label="sin(x)")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Matplotlib 2 - Scatter Plot")
plt.grid(True)
plt.legend()
plt.show()

# Histogram
x_hist = np.random.normal(0, 1, 100)
plt.figure(figsize=(10, 5))
plt.hist(x_hist, bins=20, color="red", edgecolor="black")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Matplotlib 3 - Histogram")
plt.grid(True)
plt.show()

# KDE (Manual using scipy)
x_kde = np.random.normal(0, 1, 100)
density = gaussian_kde(x_kde)
x_vals = np.linspace(min(x_kde), max(x_kde), 200)
y_vals = density(x_vals)

plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_vals, color="red", linewidth=2)
plt.fill_between(x_vals, y_vals, color="red", alpha=0.3)
plt.xlabel("x-axis")
plt.ylabel("Density")
plt.title("Matplotlib 4 - KDE (Manual)")
plt.grid(True)
plt.show()

# Bar Plot
plt.figure(figsize=(10, 5))
plt.bar(x, y, color="red")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Matplotlib 5 - Bar Plot (sin(x))")
plt.grid(True)
plt.show()

# Box Plot
x_box = np.random.normal(size=100)
plt.figure(figsize=(10, 5))
plt.boxplot(x_box, patch_artist=True)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Matplotlib 6 - Box Plot")
plt.grid(True)
plt.show()

# Violin Plot (Matplotlib)
x_violin = np.random.normal(size=100)
plt.figure(figsize=(10, 5))
plt.violinplot(x_violin, showmeans=True)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Matplotlib 7 - Violin Plot")
plt.grid(True)
plt.show()

# Combine Histogram and Line
plt.figure(figsize=(10, 5))
plt.hist(x, bins=20, alpha=0.5, color="red", edgecolor="black")
plt.plot(x, y, color="blue", label="sin(x)")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Matplotlib 8 - Histogram + Line")
plt.grid(True)
plt.legend()
plt.show()

# Combine Box Plot and Line (Subplots)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Boxplot
ax[0].boxplot(y, patch_artist=True)
ax[0].set_title("Box Plot of sin(x)")
ax[0].grid(True)

# Line Plot
ax[1].plot(x, y, color="blue")
ax[1].set_title("Line Plot of sin(x)")
ax[1].grid(True)

plt.suptitle("Matplotlib 9 - Box + Line")
plt.show()

# Combine Scatter and Line
plt.figure(figsize=(10, 5))
plt.scatter(x, y, color="red", label="Scatter")
plt.plot(x, y, color="blue", label="Line")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Matplotlib 10 - Scatter + Line")
plt.grid(True)
plt.legend()
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#global API
x = np.arange(0, 10, 0.1)
plt.figure(figsize=(10, 5))
plt.title("Matplotlib global API")

plt.subplot(1, 2, 1)
plt.plot(x, np.sin(x))
plt.grid(True)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Matplotlib 1")

plt.subplot(1, 2, 2)
plt.plot(x, np.cos(x))
plt.grid(True)
plt.xlabel("sumbu-x")
plt.ylabel("sumbu-y")
plt.title("Matplotlib 2")

plt.tight_layout()
plt.show()
#in global API we differenciate using the plt subplot, when we call it again it's not intuitive

#OOP API
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].plot(x, np.sin(x))
axes[0].grid(True)
axes[0].set_xlabel("x-axis")
axes[0].set_ylabel("y-axis")
axes[0].set_title("Matplotlib 1")

axes[1].plot(x, np.cos(x))
axes[1].grid(True)
axes[1].set_xlabel("sumbu-x")
axes[1].set_ylabel("sumbu-y")
axes[1].set_title("Matplotlib 2")

#and we can call axes 0 again

axes[0].plot(x, np.sin(x))
axes[0].grid(True)
axes[0].set_xlabel("ini x-axis")
axes[0].set_ylabel("ini y-axis")
axes[0].set_title("Matplotlib 1")

#define each linestyle and color
axes[0].plot(x, np.sin(x), color="red", linestyle="dashed")
axes[1].plot(x, np.cos(x), color="blue", linestyle="dotted")

plt.tight_layout()
plt.show()

#implement the OOP and make a subplot2grid with variating size
#use colspan and rowspan to make a subplot2grid
plt.figure(figsize=(10, 5))
ax1 = plt.subplot2grid((3, 3), (0, 0), rowspan=2, colspan=2)
ax2 = plt.subplot2grid((3, 3), (0, 2), rowspan=2, colspan=1)
ax3 = plt.subplot2grid((3, 3), (2, 0), colspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 2), colspan=1)

ax1.plot(x, np.sin(x))
ax1.set_title("Matplotlib 1")
ax2.plot(x, np.cos(x))
ax2.set_title("Matplotlib 2")
ax3.plot(x, np.sin(x))
ax3.set_title("Matplotlib 3")
ax4.plot(x, np.cos(x))
ax4.set_title("Matplotlib 4")

plt.tight_layout()
plt.show()

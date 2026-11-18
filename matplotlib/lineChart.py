import matplotlib.pyplot as plt
import pandas as pd

# 1. Sample Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sales = [20, 35, 30, 45, 40, 55, 60, 52, 70, 75, 68, 90]
profit = [10, 18, 15, 25, 22, 30, 35, 32, 40, 45, 42, 55]


# 2. Create Figure
plt.figure(figsize=(13,7), dpi=120)


# 3. Background Design
plt.gcf().set_facecolor("#0B0C0C")
ax = plt.gca()
ax.set_facecolor("#DF2222")

# 4. Plot Lines
ax.plot(
    months, sales,
    color="#43EE71",
    linewidth=8,
    marker="*",
    markersize=18,
    markerfacecolor="black",
    markeredgewidth=2,
    label="Sales"
)
ax.grid(
    True,
    linestyle="--",
    alpha=0.3,
    color="gray"
)

# 14. Display
plt.show()
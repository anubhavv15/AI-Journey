import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [30, 40, 50, 55, 70, 85]

plt.scatter(hours,marks,color="green")
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()
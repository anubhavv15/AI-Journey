import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20, 30, 25, 40, 50]

plt.fill_between(months,sales,color="purple")
plt.title("Month sale area chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

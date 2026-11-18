import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]

sales = [20, 30, 25, 40]
profit = [10, 15, 20, 25]

plt.stackplot(months,sales,profit,labels=["sales","profit"],colors=["red","black"])
plt.title("Sales and Profit")
plt.xlabel("Months")
plt.ylabel("Amount")
plt.legend()
plt.show()
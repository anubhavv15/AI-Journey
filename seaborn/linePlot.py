import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df=sns.load_dataset("tips")
sns.lineplot(data=df,x="size", y="total_bill")
plt.title("Party size vs total bill")
plt.show()
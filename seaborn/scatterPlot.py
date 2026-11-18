import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#load dataset
df=sns.load_dataset("tips")
sns.scatterplot(data=df,x="total_bill", y="tip")
plt.title("Total bill vs Tips")
plt.xlabel("Total Bill")
plt.ylabel("Tips")

plt.show()
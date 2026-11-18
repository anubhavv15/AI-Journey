import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("tips")
sns.boxplot(data=df,x="day",y="total_bill" )

plt.title("Bill Distribution By Day")
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("tips")
sns.histplot(data=df,x="total_bill", bins=25,color='red',kde=True)

plt.title("Bill Distribution")
plt.show()
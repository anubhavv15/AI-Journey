import matplotlib.pyplot as plt

subjects = ["Python", "Java", "SQL", "HTML"]
marks = [30, 25, 20, 25]

plt.pie(marks,labels=subjects,autopct="%1.1f%%",colors=['red','pink','yellow','blue'])
plt.title("Subject Distribution")
plt.show()
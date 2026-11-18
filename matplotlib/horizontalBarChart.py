import matplotlib.pyplot as plt

subjects = ["Python", "Java", "SQL", "HTML"]
marks = [85, 75, 90, 80]

plt.barh(subjects,marks,color="red")
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.show()
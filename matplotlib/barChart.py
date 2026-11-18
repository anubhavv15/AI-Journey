import matplotlib.pyplot as plt
subjects = ["Python", "Java", "SQL", "HTML"]
marks = [85, 75, 90, 80]

plt.bar(subjects,marks,color="skyblue")
plt.title("Subject Marks")
plt.xlabel("Subject")
plt.ylabel("Marks")

plt.show()
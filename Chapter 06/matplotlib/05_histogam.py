import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 62, 65, 67, 70, 72, 75, 78, 80, 85, 90]

plt.hist(marks, bins=5)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()
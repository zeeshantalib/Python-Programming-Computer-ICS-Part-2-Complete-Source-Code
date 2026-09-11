import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "PHP"]
marks = [85, 75, 65, 80]

plt.bar(subjects, marks)
#plt.barh(subjects, marks)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()
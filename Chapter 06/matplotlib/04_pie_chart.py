import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "PHP"]
students = [40, 25, 20, 15]

plt.pie(students, labels=subjects)

plt.title("Students by Programming Language")

plt.show()
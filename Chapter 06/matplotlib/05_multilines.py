import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales_2025 = [100, 150, 130, 180, 200]
sales_2026 = [120, 160, 150, 190, 230]

plt.plot(months, sales_2025, label="2025")
plt.plot(months, sales_2026, label="2026")

plt.title("Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()

plt.show()
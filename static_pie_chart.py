import matplotlib.pyplot as plt
import numpy as np

labels = input("Enter category names: ").split()

values = list(map(float, input("Enter corresponding values: ").split()))

values = np.array(values)

plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title("Dynamic Pie Chart")

plt.axis('equal')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("blood_cell_anomaly_detection.csv")

numeric_df = df.select_dtypes(include=['number'])

plt.figure()
numeric_df.boxplot()

plt.title("Boxplot of Dataset")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Write a python code for detecting missing variable

import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, np.nan, 30, 22, np.nan],
    "Salary": [50000, 60000, None, 52000, 58000]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print()

print("Missing Values (True = Missing):")
print(df.isnull())
print()

print("Total Missing Values in Each Column:")
print(df.isnull().sum())
df.to_csv("cleaned_dataset.csv", index=False)
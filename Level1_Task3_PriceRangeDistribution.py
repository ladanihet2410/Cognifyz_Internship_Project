import pandas as pd
import matplotlib.pyplot as plt

file_path = "D:\Internship\Dataset .csv"
df = pd.read_csv(file_path)

price_counts = df["Price range"].value_counts().sort_index()

price_counts.plot(kind="bar")
plt.title("Price Range Distribution")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.show()

percentage = (price_counts / len(df)) * 100
print(percentage)

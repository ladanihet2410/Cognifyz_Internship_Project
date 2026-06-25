import pandas as pd
import matplotlib.pyplot as plt

file_path = "D:\Internship\Dataset .csv"
df = pd.read_csv(file_path)

df["Aggregate rating"].hist(bins=10)
plt.title("Rating Distribution")
plt.show()

rating_range = pd.cut(df["Aggregate rating"], bins=[0,1,2,3,4,5])
print(rating_range.value_counts())

print("Average Votes:", df["Votes"].mean())

import pandas as pd

file_path = "D:\Internship\Dataset .csv"
df = pd.read_csv(file_path)

city_count = df["City"].value_counts()
print("City with highest number of restaurants:")
print(city_count.idxmax())

avg_rating = df.groupby("City")["Aggregate rating"].mean().sort_values(ascending=False)
print("\nAverage Rating by City")
print(avg_rating)

print("\nCity with Highest Average Rating")
print(avg_rating.idxmax())

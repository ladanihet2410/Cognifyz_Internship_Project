import pandas as pd

file_path = "D:\Internship\Dataset .csv"
df = pd.read_csv(file_path)

delivery_percentage = (df["Has Online delivery"].eq("Yes").sum() / len(df)) * 100
print("Online Delivery Percentage:", round(delivery_percentage,2))

avg_rating = df.groupby("Has Online delivery")["Aggregate rating"].mean()
print(avg_rating)

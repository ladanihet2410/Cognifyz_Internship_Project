import pandas as pd

file_path = r"D:\Internship\Dataset .csv"
df = pd.read_csv(file_path)

cuisines = df["Cuisines"].dropna().str.split(", ").explode()
top_cuisines = cuisines.value_counts().head(3)

total_restaurants = len(df)

print("Top 3 Cuisines")
for cuisine, count in top_cuisines.items():
    percentage = (count / total_restaurants) * 100
    print(f"{cuisine}: {count} restaurants ({percentage:.2f}%)")

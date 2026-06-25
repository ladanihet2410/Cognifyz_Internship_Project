import pandas as pd

file_path = "D:\Internship\Dataset .csv"
df = pd.read_csv(file_path)

top_combinations = df["Cuisines"].value_counts().head(10)
print(top_combinations)

rating_analysis = df.groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False)
print(rating_analysis.head(10))

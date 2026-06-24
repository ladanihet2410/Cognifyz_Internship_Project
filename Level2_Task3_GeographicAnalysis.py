import pandas as pd
import matplotlib.pyplot as plt

file_path = r"D:\Internship\Dataset .csv"
df = pd.read_csv(file_path)

# remove rows where coordinates are missing
df = df.dropna(subset=["Longitude", "Latitude"])

# plot restaurant locations
plt.figure(figsize=(10, 6))
plt.scatter(df["Longitude"], df["Latitude"], alpha=0.5)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Restaurant Locations")
plt.show()

# identify clusters by counting restaurants at same coordinates
location_counts = df.groupby(["Longitude", "Latitude"]).size().reset_index(name="Restaurant Count")

# top clustered locations
print("Top restaurant clusters based on same coordinates:")
print(location_counts.sort_values(by="Restaurant Count", ascending=False).head(10))
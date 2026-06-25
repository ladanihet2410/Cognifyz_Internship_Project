import pandas as pd

file_path = "D:\Internship\Dataset .csv"
df = pd.read_csv(file_path)

chains = df["Restaurant Name"].value_counts()
chains = chains[chains > 1]

print("Restaurant Chains")
print(chains.head(20))

chain_data = df.groupby("Restaurant Name").agg({
    "Aggregate rating":"mean",
    "Votes":"sum"
})

print(chain_data.loc[chains.index].sort_values("Votes", ascending=False).head(20))

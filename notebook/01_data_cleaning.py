import pandas as pd

# Load data
matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

print("=" * 50)
print("MATCHES DATASET")
print("=" * 50)

print("Shape:", matches.shape)

print("\nMissing Values:")
print(matches.isnull().sum())

print("\nDuplicate Rows:")
print(matches.duplicated().sum())

print("\n")

print("=" * 50)
print("DELIVERIES DATASET")
print("=" * 50)

print("Shape:", deliveries.shape)

print("\nMissing Values:")
print(deliveries.isnull().sum())

print("\nDuplicate Rows:")
print(deliveries.duplicated().sum())

# Team name standardization
team_mapping = {
    "Delhi Daredevils": "Delhi Capitals",
    "Kings XI Punjab": "Punjab Kings",
    "Royal Challengers Bangalore": "Royal Challengers Bengaluru"
}

for col in ["team1", "team2", "toss_winner", "winner"]:
    matches[col] = matches[col].replace(team_mapping)

for col in ["batting_team", "bowling_team"]:
    deliveries[col] = deliveries[col].replace(team_mapping)

# Save cleaned files
matches.to_csv("data/clean_matches.csv", index=False)
deliveries.to_csv("data/clean_deliveries.csv", index=False)

print("\nCleaned files saved successfully!")
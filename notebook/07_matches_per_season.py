import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("data/clean_matches.csv")

season_matches = matches.groupby("season").size()

plt.figure(figsize=(10,5))

season_matches.plot(
    marker="o"
)

plt.title("Matches Played Per Season")
plt.xlabel("Season")
plt.ylabel("Matches")

plt.grid(True)

plt.savefig(
    "outputs/charts/matches_per_season.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(season_matches)
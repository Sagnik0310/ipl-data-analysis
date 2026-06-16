import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("data/clean_matches.csv")
deliveries = pd.read_csv("data/clean_deliveries.csv")

merged = deliveries.merge(
    matches[["match_id", "season"]],
    on="match_id"
)

season_runs = merged.groupby("season")["total_runs"].sum()

plt.figure(figsize=(10,5))
season_runs.plot(marker="o")

plt.title("Total Runs Scored Per IPL Season")
plt.xlabel("Season")
plt.ylabel("Runs")

plt.grid(True)

plt.savefig(
    "outputs/charts/runs_per_season.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(season_runs)
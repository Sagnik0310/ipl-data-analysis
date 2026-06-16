import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("data/clean_matches.csv")

venues = matches["venue"].value_counts()

print("\nTOP VENUES")
print(venues.head(10))

plt.figure(figsize=(12,6))

venues.head(10).plot(kind="bar")

plt.title("Top IPL Venues")
plt.xlabel("Venue")
plt.ylabel("Matches Hosted")

plt.tight_layout()

plt.savefig(
    "outputs/charts/top_venues.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
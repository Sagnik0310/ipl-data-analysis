import pandas as pd
import matplotlib.pyplot as plt

# Load data
deliveries = pd.read_csv("data/clean_deliveries.csv")
matches = pd.read_csv("data/clean_matches.csv")

print("DELIVERIES COLUMNS:")
print(deliveries.columns.tolist())

print("\nMATCHES COLUMNS:")
print(matches.columns.tolist())

# =====================================
# TOP 10 RUN SCORERS
# =====================================

runs = deliveries.groupby("striker")["batsman_runs"].sum()
runs = runs.sort_values(ascending=False)

print("\nTOP 10 RUN SCORERS")
print(runs.head(10))

plt.figure(figsize=(12,6))
runs.head(10).plot(kind="bar")

plt.title("Top 10 IPL Run Scorers")
plt.xlabel("Player")
plt.ylabel("Runs")

plt.tight_layout()

plt.savefig(
    "outputs/charts/top_run_scorers.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# =====================================
# TOP WICKET TAKERS
# =====================================

try:
    wickets = deliveries[deliveries["is_wicket"] == 1]

    top_wickets = wickets.groupby("bowler").size()
    top_wickets = top_wickets.sort_values(ascending=False)

    print("\nTOP 10 WICKET TAKERS")
    print(top_wickets.head(10))

    plt.figure(figsize=(12,6))

    top_wickets.head(10).plot(kind="bar")

    plt.title("Top 10 IPL Wicket Takers")
    plt.xlabel("Bowler")
    plt.ylabel("Wickets")

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/top_wicket_takers.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("top_wicket_takers.png created")

except Exception as e:
    print("WICKET ANALYSIS ERROR:")
    print(e)

# =====================================
# PLAYER OF MATCH
# =====================================

try:
    pom = matches["player_of_match"].value_counts()

    print("\nTOP PLAYER OF MATCH WINNERS")
    print(pom.head(10))

    plt.figure(figsize=(12,6))

    pom.head(10).plot(kind="bar")

    plt.title("Most Player of Match Awards")
    plt.xlabel("Player")
    plt.ylabel("Awards")

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/player_of_match.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("player_of_match.png created")

except Exception as e:
    print("PLAYER OF MATCH ERROR:")
    print(e)

print("\nPlayer analysis completed successfully.")
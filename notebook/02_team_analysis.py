import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("data/clean_matches.csv")

# Team wins
wins = matches['winner'].value_counts()

print("\nTEAM WINS")
print(wins)

plt.figure(figsize=(12,6))

wins.plot(kind='bar')

plt.title("Most Successful IPL Teams")
plt.xlabel("Teams")
plt.ylabel("Wins")

plt.tight_layout()

plt.savefig(
    "outputs/charts/team_wins.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Toss impact analysis

toss_match = matches[
    matches['toss_winner'] == matches['winner']
]

percentage = (
    len(toss_match) /
    len(matches)
) * 100

print("\nToss Winner Won Match:")
print(f"{percentage:.2f}%")

plt.figure(figsize=(6,6))

sizes = [
    len(toss_match),
    len(matches)-len(toss_match)
]

labels = [
    "Toss Winner Won",
    "Toss Winner Lost"
]

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Impact of Toss")

plt.savefig(
    "outputs/charts/toss_impact.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Better chart styling
sns.set_style("whitegrid")

# Load data
matches = pd.read_csv("data/clean_matches.csv")
deliveries = pd.read_csv("data/clean_deliveries.csv")

# ==========================================
# 1. TEAM WINS (SEABORN)
# ==========================================

wins = matches['winner'].value_counts().head(10)

wins_df = wins.reset_index()
wins_df.columns = ['Team', 'Wins']

plt.figure(figsize=(12,6))

sns.barplot(
    data=wins_df,
    x='Team',
    y='Wins'
)

plt.xticks(rotation=45)
plt.title("Top IPL Teams by Wins")

plt.tight_layout()

plt.savefig(
    "outputs/charts/team_wins_seaborn.png",
    dpi=300
)

plt.close()

print("team_wins_seaborn.png created")

# ==========================================
# 2. TOP RUN SCORERS
# ==========================================

runs = deliveries.groupby(
    "striker"
)["batsman_runs"].sum()

runs = runs.sort_values(
    ascending=False
).head(10)

runs_df = runs.reset_index()
runs_df.columns = ['Player', 'Runs']

plt.figure(figsize=(12,6))

sns.barplot(
    data=runs_df,
    x='Player',
    y='Runs'
)

plt.xticks(rotation=45)

plt.title("Top 10 IPL Run Scorers")

plt.tight_layout()

plt.savefig(
    "outputs/charts/top_run_scorers_seaborn.png",
    dpi=300
)

plt.close()

print("top_run_scorers_seaborn.png created")

# ==========================================
# 3. TOP WICKET TAKERS
# ==========================================

wickets = deliveries[
    deliveries["is_wicket"] == 1
]

top_wickets = wickets.groupby(
    "bowler"
).size()

top_wickets = top_wickets.sort_values(
    ascending=False
).head(10)

wickets_df = top_wickets.reset_index()
wickets_df.columns = ['Bowler', 'Wickets']

plt.figure(figsize=(12,6))

sns.barplot(
    data=wickets_df,
    x='Bowler',
    y='Wickets'
)

plt.xticks(rotation=45)

plt.title("Top 10 IPL Wicket Takers")

plt.tight_layout()

plt.savefig(
    "outputs/charts/top_wicket_takers_seaborn.png",
    dpi=300
)

plt.close()

print("top_wicket_takers_seaborn.png created")

# ==========================================
# 4. PLAYER OF MATCH
# ==========================================

pom = matches[
    "player_of_match"
].value_counts().head(10)

pom_df = pom.reset_index()
pom_df.columns = ['Player', 'Awards']

plt.figure(figsize=(12,6))

sns.barplot(
    data=pom_df,
    x='Player',
    y='Awards'
)

plt.xticks(rotation=45)

plt.title("Most Player of Match Awards")

plt.tight_layout()

plt.savefig(
    "outputs/charts/player_of_match_seaborn.png",
    dpi=300
)

plt.close()

print("player_of_match_seaborn.png created")

# ==========================================
# 5. CORRELATION HEATMAP
# ==========================================

numeric_columns = [
    "first_innings_score",
    "first_innings_wickets",
    "second_innings_score",
    "second_innings_wickets",
    "win_margin"
]

available_columns = [
    col for col in numeric_columns
    if col in matches.columns
]

if len(available_columns) > 1:

    correlation = matches[
        available_columns
    ].corr()

    plt.figure(figsize=(8,6))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm"
    )

    plt.title(
        "IPL Statistics Correlation Heatmap"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/correlation_heatmap.png",
        dpi=300
    )

    plt.close()

    print("correlation_heatmap.png created")

else:
    print("Not enough numeric columns for heatmap")

print("\nSeaborn analysis completed successfully.")
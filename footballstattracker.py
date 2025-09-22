# Simple Football Running Back Statistic Sheet

# Define running back stats
running_back_stats = {
    "Name": "John Doe",
    "Team": "Wildcats",
    "Games Played": 12,
    "Rushing Attempts": 210,
    "Rushing Yards": 1120,
    "Rushing Touchdowns": 10,
    "Receptions": 35,
    "Receiving Yards": 280,
    "Receiving Touchdowns": 2,
    "Fumbles": 3
}

# Display the stats
print("Football Running Back Statistic Sheet")
print("-" * 40)
for stat, value in running_back_stats.items():
    print(f"{stat:22}: {value}")
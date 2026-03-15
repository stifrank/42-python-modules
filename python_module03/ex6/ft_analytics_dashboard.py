print("=== Game Analytics Dashboard ===")

players = ["alice", "bob", "charlie", "diana"]

scores = {
    "alice": 2300,
    "bob": 1800,
    "charlie": 2150,
    "diana": 1900,
}

achievements = {
    "alice": {
        "first_kill",
        "level_10",
        "boss_slayer",
        "speed_demon",
        "treasure_hunter",
    },
    "bob": {
        "first_kill",
        "level_10",
        "collector",
    },
    "charlie": {
        "level_10",
        "boss_slayer",
        "perfectionist",
        "speed_demon",
        "treasure_hunter",
        "elite",
    },
    "diana": {
        "first_kill",
        "explorer",
    },
}

print("=== List Comprehension Examples ===")

high_scorers = [player for player in players if scores[player] > 2000]
print(f"High scorers (>2000): {high_scorers}")

scores_doubled = [scores[player] * 2 for player in players]
print(f"Scores doubled: {scores_doubled}")

active_players = [player for player in players if len(achievements[player]) > 0]
print(f"Active players: {active_players}")

print("=== Dict Comprehension Examples ===")

player_scores = {player: scores[player] for player in players}
print(f"Player scores: {player_scores}")

achievement_counts = {
    player: len(achievements[player]) for player in players
}
print(f"Achievement counts: {achievement_counts}")

score_labels = {
    player: (
        "high"
        if scores[player] >= 2100
        else "medium"
        if scores[player] >= 1800
        else "low"
    )
    for player in players
}
print(f"Score labels: {score_labels}")

print("=== Set Comprehension Examples ===")

unique_players = {player for player in players}
print(f"Unique players: {unique_players}")

unique_achievements = {
    achievement
    for player in players
    for achievement in achievements[player]
}
print(f"Unique achievements: {unique_achievements}")

active_regions = {region for region in ["north", "east", "central", "east", "north"]}
print(f"Active regions: {active_regions}")

print("=== Combined Analysis ===")

total_players = len(players)
total_unique_achievements = len(unique_achievements)
average_score = sum([scores[player] for player in players]) / len(players)

sorted_players = sorted(players, key=lambda player: scores[player], reverse=True)
top_player = sorted_players[0]

print(f"Total players: {total_players}")
print(f"Total unique achievements: {total_unique_achievements}")
print(f"Average score: {average_score}")
print(
    f"Top performer: {top_player} "
    f"({scores[top_player]} points, {len(achievements[top_player])} achievements)"
)
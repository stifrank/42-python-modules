print("=== Game Analytics Dashboard ===")

players = ["alice", "bob", "charlie", "diana"]

scores = {
    "alice": 2300,
    "bob": 1800,
    "charlie": 2150,
    "diana": 1900,
}

achievements = {
    "alice": {"first_kill", "level_10", "boss_slayer", "speed_demon", "treasure_hunter"},
    "bob": {"first_kill", "level_10", "collector"},
    "charlie": {"level_10", "boss_slayer", "perfectionist", "speed_demon", "treasure_hunter", "elite"},
    "diana": {"first_kill", "explorer"},
}

# === List Comprehension Examples ===
print("=== List Comprehension Examples ===")

high_scorers = [p for p, s in scores.items() if s > 2000]
print(f"High scorers (>2000): {high_scorers}")

scores_doubled = [s * 2 for s in scores.values()]
print(f"Scores doubled: {scores_doubled}")

active_players = [p for p in players if p in achievements]
print(f"Active players: {active_players}")

# === Dict Comprehension Examples ===
print("=== Dict Comprehension Examples ===")

player_scores = {p: scores[p] for p in players}
print(f"Player scores: {player_scores}")

score_categories = {
    "high": len([s for s in scores.values() if s >= 2100]),
    "medium": len([s for s in scores.values() if 1800 <= s < 2100]),
    "low": len([s for s in scores.values() if s < 1800]),
}
print(f"Score categories: {score_categories}")

achievement_counts = {p: len(a) for p, a in achievements.items()}
print(f"Achievement counts: {achievement_counts}")

# === Set Comprehension Examples ===
print("=== Set Comprehension Examples ===")

unique_players = {p for p in players}
print(f"Unique players: {unique_players}")

unique_achievements = {ach for aset in achievements.values() for ach in aset}
print(f"Unique achievements: {unique_achievements}")

active_regions = {r for r in ["north", "east", "central", "east", "north"]}
print(f"Active regions: {active_regions}")

# === Combined Analysis ===
print("=== Combined Analysis ===")

total_players = len(players)
total_unique_achievements = len(unique_achievements)
average_score = sum(scores.values()) / len(scores)
top_player = max(scores, key=scores.get)

print(f"Total players: {total_players}")
print(f"Total unique achievements: {total_unique_achievements}")
print(f"Average score: {average_score}")
print(f"Top performer: {top_player} ({scores[top_player]} points, {len(achievements[top_player])} achievements)")

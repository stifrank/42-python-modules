import random

print("=== Game Data Alchemist ===")
print()

players = [
    "Alice", "bob", "Charlie", "dylan",
    "Emma", "Gregory", "john", "kevin", "Liam"
]

print(f"Initial list of players: {players}")

all_capitalized = [name.capitalize() for name in players]
print(f"New list with all names capitalized: {all_capitalized}")

capitalized_only = [name for name in players if name[0].isupper()]
print(f"New list of capitalized names only: {capitalized_only}")
print()

scores = {name: random.randint(0, 1000) for name in all_capitalized}
print(f"Score dict: {scores}")

average = sum(scores.values()) / len(scores)
print(f"Score average is {round(average, 2)}")

high_scores = {
    name: score for name, score in scores.items()
    if score > average
}
print(f"High scores: {high_scores}")
print()

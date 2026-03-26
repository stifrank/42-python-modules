import random

print("=== Achievement Tracker System ===\n")


def gen_player_achievements():
    all_achievements = [
        "First Steps",
        "Speed Runner",
        "Boss Slayer",
        "Treasure Hunter",
        "Master Explorer",
        "Collector Supreme",
        "World Savior",
        "Strategist",
        "Untouchable",
        "Crafting Genius",
        "Sharp Mind",
        "Survivor",
        "Unstoppable",
        "Hidden Path Finder",
    ]

    count = random.randint(5, 9)
    return set(random.sample(all_achievements, count))


alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()

print(f"Player Alice: {alice}")
print(f"Player Bob: {bob}")
print(f"Player Charlie: {charlie}")
print(f"Player Dylan: {dylan}")
print()

all_distinct = alice.union(bob).union(charlie).union(dylan)
print(f"All distinct achievements: {all_distinct}")
print()

common = alice.intersection(bob).intersection(charlie).intersection(dylan)
print(f"Common achievements: {common}")
print()

only_alice = alice.difference(bob.union(charlie).union(dylan))
only_bob = bob.difference(alice.union(charlie).union(dylan))
only_charlie = charlie.difference(alice.union(bob).union(dylan))
only_dylan = dylan.difference(alice.union(bob).union(charlie))

print(f"Only Alice has: {only_alice}")
print(f"Only Bob has: {only_bob}")
print(f"Only Charlie has: {only_charlie}")
print(f"Only Dylan has: {only_dylan}")
print()

alice_missing = all_distinct.difference(alice)
bob_missing = all_distinct.difference(bob)
charlie_missing = all_distinct.difference(charlie)
dylan_missing = all_distinct.difference(dylan)

print(f"Alice is missing: {alice_missing}")
print(f"Bob is missing: {bob_missing}")
print(f"Charlie is missing: {charlie_missing}")
print(f"Dylan is missing: {dylan_missing}")
print()

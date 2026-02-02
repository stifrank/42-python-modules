print("=== Achievement Tracker System ===")

alice = set(["first_kill", "level_10", "treasure_hunter", "speed_demon"])
bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
charlie = set(["level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"])

print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

print("=== Achievement Analytics ===")

# 1) Todos los logros únicos (union)
all_unique = alice.union(bob).union(charlie)
print(f"All unique achievements: {all_unique}")
print(f"Total unique achievements: {len(all_unique)}")

# 2) Comunes a todos (intersection)
common_all = alice.intersection(bob).intersection(charlie)
print(f"Common to all players: {common_all}")

# 3) Raros: aparecen en EXACTAMENTE 1 jugador
rare_alice = alice.difference(bob).difference(charlie)
rare_bob = bob.difference(alice).difference(charlie)
rare_charlie = charlie.difference(alice).difference(bob)
rare = rare_alice.union(rare_bob).union(rare_charlie)
print(f"Rare achievements (1 player): {rare}")

# 4) Comparación Alice vs Bob
print(f"Alice vs Bob common: {alice.intersection(bob)}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")

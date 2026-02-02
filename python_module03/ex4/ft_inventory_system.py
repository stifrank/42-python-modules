print("=== Player Inventory System ===")

inventories = dict({
    "alice": dict({
        "sword": dict({"type": "weapon", "rarity": "rare", "qty": 1, "value": 500}),
        "potion": dict({"type": "consumable", "rarity": "common", "qty": 5, "value": 50}),
        "shield": dict({"type": "armor", "rarity": "uncommon", "qty": 1, "value": 200}),
    }),
    "bob": dict({
        "potion": dict({"type": "consumable", "rarity": "common", "qty": 0, "value": 50}),
        "magic_ring": dict({"type": "accessory", "rarity": "rare", "qty": 1, "value": 600}),
    }),
})


def print_inventory(player_name, inv):
    print(f"=== {player_name.capitalize()}'s Inventory ===")

    total_value = 0
    total_items = 0
    categories = dict({})

    for item_name, info in inv.items():
        qty = info.get("qty")
        value = info.get("value")
        item_type = info.get("type")
        rarity = info.get("rarity")

        line_value = qty * value
        total_value += line_value
        total_items += qty

        if categories.get(item_type) is None:
            categories.update({item_type: qty})
        else:
            categories.update({item_type: categories.get(item_type) + qty})

        print(f"{item_name} ({item_type}, {rarity}): {qty}x @ {value} gold each = {line_value} gold")

    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {total_items} items")

    cat_parts = []
    for cat, qty in categories.items():
        cat_parts.append(f"{cat}({qty})")
    print("Categories: " + ", ".join(cat_parts))

    return total_value, total_items


# 1) Mostrar inventario de Alice
alice_inv = inventories.get("alice")
print_inventory("alice", alice_inv)

# 2) Transacción: Alice da a Bob 2 potions
print("=== Transaction: Alice gives Bob 2 potions ===")

alice_potion = alice_inv.get("potion")
bob_inv = inventories.get("bob")
bob_potion = bob_inv.get("potion")

if alice_potion is not None and bob_potion is not None and alice_potion.get("qty") >= 2:
    alice_potion.update({"qty": alice_potion.get("qty") - 2})
    bob_potion.update({"qty": bob_potion.get("qty") + 2})
    print("Transaction successful!")
else:
    print("Transaction failed!")

print("=== Updated Inventories ===")
print(f"Alice potions: {alice_inv.get('potion').get('qty')}")
print(f"Bob potions: {bob_inv.get('potion').get('qty')}")

# 3) Analytics global
print("=== Inventory Analytics ===")

values = dict({})
items_count = dict({})

for player, inv in inventories.items():
    total_value = 0
    total_items = 0
    for _, info in inv.items():
        total_value += info.get("qty") * info.get("value")
        total_items += info.get("qty")
    values.update({player: total_value})
    items_count.update({player: total_items})

# Most valuable player
most_valuable = None
most_value = -1
for player, val in values.items():
    if val > most_value:
        most_value = val
        most_valuable = player
print(f"Most valuable player: {most_valuable.capitalize()} ({most_value} gold)")

# Most items
most_items_player = None
most_items = -1
for player, cnt in items_count.items():
    if cnt > most_items:
        most_items = cnt
        most_items_player = player
print(f"Most items: {most_items_player.capitalize()} ({most_items} items)")

# Rarest items (por rareza = 'rare', listado por nombre)
rare_names = set()
for _, inv in inventories.items():
    for item_name, info in inv.items():
        if info.get("rarity") == "rare":
            rare_names = rare_names.union(set([item_name]))

print("Rarest items: " + ", ".join(rare_names))

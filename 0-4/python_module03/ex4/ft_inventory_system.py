import sys

print("=== Inventory System Analysis ===")

inventory = {}

i = 1
while i < len(sys.argv):
    arg = sys.argv[i]

    if ":" not in arg:
        print(f"Error- invalid parameter '{arg}'")
        i += 1
        continue

    parts = arg.split(":")

    if len(parts) != 2:
        print(f"Error- invalid parameter '{arg}'")
        i += 1
        continue

    name = parts[0]
    qty_str = parts[1]

    if name in inventory:
        print(f"Redundant item '{name}'- discarding")
        i += 1
        continue

    try:
        qty = int(qty_str)
    except ValueError as e:
        print(f"Quantity error for '{name}': {e}")
        i += 1
        continue

    inventory.update({name: qty})

    i += 1


print(f"Got inventory: {inventory}")

item_list = list(inventory.keys())
print(f"Item list: {item_list}")

total = sum(inventory.values())
print(f"Total quantity of the {len(inventory)} items: {total}")

for item in inventory:
    percent = (inventory[item] / total) * 100
    print(f"Item {item} represents {round(percent, 1)}%")

most_item = None
least_item = None

for item in inventory:
    if most_item is None:
        most_item = item
        least_item = item
    else:
        if inventory[item] > inventory[most_item]:
            most_item = item
        if inventory[item] < inventory[least_item]:
            least_item = item

print(
    f"Item most abundant: {most_item} "
    f"with quantity {inventory[most_item]}"
)

print(
    f"Item least abundant: {least_item} "
    f"with quantity {inventory[least_item]}"
)

inventory.update({"magic_item": 1})

print(f"Updated inventory: {inventory}")

import sys

print("=== Inventory System Analysis ===")

if len(sys.argv) == 1:
    print(
        "No inventory provided. Usage: "
        "python3 ft_inventory_system.py sword:1 potion:5 shield:2"
    )
else:
    item_data = dict({
        "sword": dict({"type": "weapon", "value": 100}),
        "potion": dict({"type": "consumable", "value": 20}),
        "shield": dict({"type": "armor", "value": 80}),
        "armor": dict({"type": "armor", "value": 120}),
        "helmet": dict({"type": "armor", "value": 60}),
    })

    inventory = dict({})

    i = 1
    while i < len(sys.argv):
        parts = sys.argv[i].split(":")
        if len(parts) == 2:
            item_name = parts[0]
            quantity = int(parts[1])

            item_info = item_data.get(
                item_name,
                dict({"type": "unknown", "value": 0})
            )

            inventory.update({
                item_name: dict({
                    "name": item_name,
                    "type": item_info.get("type"),
                    "quantity": quantity,
                    "value": item_info.get("value"),
                })
            })
        i += 1

    total_items = 0
    for info in inventory.values():
        total_items += info.get("quantity")

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("=== Current Inventory ===")
    for item_name, info in inventory.items():
        quantity = info.get("quantity")
        percentage = (quantity / total_items) * 100
        print(f"{item_name}: {quantity} units ({percentage:.1f}%)")

    most_abundant = None
    least_abundant = None

    for item_name, info in inventory.items():
        if most_abundant is None:
            most_abundant = item_name
            least_abundant = item_name
        else:
            if (
                info.get("quantity")
                > inventory.get(most_abundant).get("quantity")
            ):
                most_abundant = item_name
            if (
                info.get("quantity")
                < inventory.get(least_abundant).get("quantity")
            ):
                least_abundant = item_name

    print("=== Inventory Statistics ===")
    print(
        f"Most abundant: {most_abundant} "
        f"({inventory.get(most_abundant).get('quantity')} units)"
    )
    print(
        f"Least abundant: {least_abundant} "
        f"({inventory.get(least_abundant).get('quantity')} units)"
    )

    abundant = dict({})
    moderate = dict({})
    scarce = dict({})

    for item_name, info in inventory.items():
        quantity = info.get("quantity")
        if quantity >= 6:
            abundant.update({item_name: quantity})
        elif quantity >= 4:
            moderate.update({item_name: quantity})
        else:
            scarce.update({item_name: quantity})

    print("=== Item Categories ===")
    if len(abundant) > 0:
        print(f"Abundant: {abundant}")
    if len(moderate) > 0:
        print(f"Moderate: {moderate}")
    if len(scarce) > 0:
        print(f"Scarce: {scarce}")

    restock = []

    for item_name, info in inventory.items():
        if info.get("quantity") <= 1:
            restock.append(item_name)

    print("=== Management Suggestions ===")
    if len(restock) > 0:
        print("Restock needed: " + ", ".join(restock))
    else:
        print("No restock needed.")

    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys: " + ", ".join(inventory.keys()))

    values_text = []
    for info in inventory.values():
        values_text.append(str(info.get("quantity")))
    print("Dictionary values: " + ", ".join(values_text))

    print(
        "Sample lookup - 'sword' in inventory: "
        f"{inventory.get('sword') is not None}"
    )
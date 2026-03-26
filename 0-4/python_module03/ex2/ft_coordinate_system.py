import math

print("=== Game Coordinate System ===")


def get_player_pos():
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        parts = user_input.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coords = []

        i = 0
        while i < 3:
            value = parts[i].strip()
            try:
                coords.append(float(value))
            except ValueError as e:
                print(f"Error on parameter '{value}': {e}")
                break
            i += 1

        if len(coords) == 3:
            return (coords[0], coords[1], coords[2])


print("Get a first set of coordinates")

pos1 = get_player_pos()

print(f"Got a first tuple: {pos1}")
print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

distance_center = math.sqrt(
    (pos1[0])**2 + (pos1[1])**2 + (pos1[2])**2
)

print(f"Distance to center: {round(distance_center, 4)}")
print()


print("Get a second set of coordinates")

pos2 = get_player_pos()

distance_between = math.sqrt(
    (pos2[0] - pos1[0])**2 +
    (pos2[1] - pos1[1])**2 +
    (pos2[2] - pos1[2])**2
)

print(
    "Distance between the 2 sets of coordinates: "
    f"{round(distance_between, 4)}"
)
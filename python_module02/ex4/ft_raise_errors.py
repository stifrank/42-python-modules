"""
Module 02 - ex4: Raising errors.

Uses raise to signal invalid plant health conditions.
"""


def check_plant_health(plant_name, water_level, sunlight_hours):
    """Validate plant health values and raise errors when invalid."""

    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
                        f"Sunlight hours {sunlight_hours} "
                        f"is too high (max 12)"
        )

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """Demonstrate error raising and handling for plant health checks."""
    print("=== Garden Plant Health Checker ===")
    print()

    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 5, 8)
        print(result)
        print()
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except ValueError as e:
        print(f"Error: {e}")
        print()

    print("Testing bad water level...")
    try:
        check_plant_health("lettuce", 15, 8)
    except ValueError as e:
        print(f"Error: {e}")
        print()

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("carrots", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")
        print()

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()

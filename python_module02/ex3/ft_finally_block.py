"""
Module 02 - ex3: Finally block.

Demonstrates using finally to ensure cleanup always occurs.
"""


def water_plants(plant_list):
    """Water plants and always close the watering system using finally."""

    print("Opening watering system")
    try:
        for plant in plant_list:
            try:
                plant_name = plant.lower()
                print(f"Watering {plant_name}")
            except Exception:
                print(f"Error: Cannot water {plant} - invalid plant!")
                return
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Demonstrate cleanup behavior with valid and invalid plant lists."""

    print("=== Garden Watering System ===")
    print()

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print()

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

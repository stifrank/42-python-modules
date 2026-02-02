"""
Module 02 - ex5: Garden management.

Combines custom errors, raise, try/except, and finally in a garden system.
"""

class GardenError(Exception):
	"""Base exception for garden management errors."""

    pass


class PlantError(GardenError):
	"""Exception raised when plant data is invalid."""

    pass


class WaterError(GardenError):
	"""Exception raised for watering system failures."""

    pass


class GardenManager:
	"""Manage plants and handle garden operations safely."""

    def __init__(self):
		"""Initialize the garden manager with an empty plant list."""
		
        self.plants = []

    def add_plant(self, plant_name, water_level, sunlight_hours):
		"""Add a plant to the garden or raise an error if invalid."""

        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(
            {
                "name": plant_name,
                "water": water_level,
                "sun": sunlight_hours,
            }
        )
        print(f"Added {plant_name} successfully")

    def water_plants(self):
		"""Water all plants and always clean up the watering system."""

        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant['name']} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
		"""Check health conditions for a single plant."""
    
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")

        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")

        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")

        print(f"{plant_name}: healthy (water: {water_level}, sun: {sunlight_hours})")

    def check_all_health(self):
		"""Check health conditions for all plants in the garden."""

        print("Checking plant health...")
        for plant in self.plants:
            try:
                self.check_plant_health(plant["name"], plant["water"], plant["sun"])
            except ValueError as e:
                print(f"Error checking {plant['name']}: {e}")


def test_garden_management():
	"""Demonstrate full garden management with error handling and cleanup."""

    print("=== Garden Management System ===")
    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato", 5, 8)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    try:
        manager.add_plant("lettuce", 15, 8)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    try:
        manager.add_plant("", 5, 8)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    print("Watering plants...")
    manager.water_plants()

    manager.check_all_health()

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()

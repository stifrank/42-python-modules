class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name, water_level, sunlight_hours):
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
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant['name']} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        # Reglas del ex4, pero aquí dentro del gestor
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
        print("Checking plant health...")
        for plant in self.plants:
            try:
                self.check_plant_health(plant["name"], plant["water"], plant["sun"])
            except ValueError as e:
                print(f"Error checking {plant['name']}: {e}")


def test_garden_management():
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

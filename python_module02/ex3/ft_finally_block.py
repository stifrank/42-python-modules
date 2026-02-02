def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            try:
                plant_name = plant.lower()
                print(f"Watering {plant_name}")
            except:
                print(f"Error: Cannot water {plant} - invalid plant!")
                return
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

"""
Module 02 - ex2: Custom errors.

Defines custom exception classes and demonstrates raising and catching them.
"""

class GardenError(Exception):
	"""Base exception for garden-related errors."""

    pass


class PlantError(GardenError):
	"""Exception raised for plant-related issues."""

    pass


class WaterError(GardenError):
	"""Exception raised for watering-related issues."""

    pass


def trigger_plant_error():
	"""Raise a PlantError to simulate a plant-related failure."""

    raise PlantError("The tomato plant is wilting!")


def trigger_water_error():
	"""Raise a WaterError to simulate a watering-related failure."""

    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
	"""Demonstrate catching specific and base custom exceptions."""
	
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        trigger_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        trigger_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    for test in (trigger_plant_error, trigger_water_error):
        try:
            test()
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()

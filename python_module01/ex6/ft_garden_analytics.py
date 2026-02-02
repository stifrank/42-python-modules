"""
Module 01 - ex6: Garden analytics.

Analyzes multiple plants to compute average statistics.
"""

class Plant:
	"""Represent a plant used for garden analysis."""

    def __init__(self, name: str, height: int, age: int):
		"""Initialize plant attributes."""

        self._name = name
        self._height = height
        self._age = age

    def get_height(self):
		"""Return the plant height."""

        return self._height

    def get_age(self):
		"""Return the plant age."""

        return self._age

    def display_info(self):
		"""Display plant information."""
		
        print(f"{self._name}: {self._height}cm, {self._age} days old")

if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]

    total_height = 0
    total_age = 0

    for plant in plants:
        plant.display_info()
        total_height += plant.get_height()
        total_age += plant.get_age()

    avg_height = total_height / len(plants)
    avg_age = total_age / len(plants)

    print("\nGarden analytics:")
    print(f"Average height: {avg_height}cm")
    print(f"Average age: {avg_age} days")
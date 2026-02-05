"""
Module 01 - ex3: Plant factory.

This script defines a PlantFactory class responsible for creating Plant
objects, tracking how many plants have been created, and printing the factory
output exactly as specified in the subject example.
"""


class Plant:
    """
    Represents a plant with a name, height in centimeters, and age in days.
    """

    def __init__(self, name, height_cm, age_days):
        """
        Initializes a plant with its basic attributes.
        """

        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days


class PlantFactory:
    """
    Factory responsible for creating plants and counting them.
    """

    def __init__(self):
        """
        Initializes the plant factory with zero created plants.
        """

        self.count = 0

    def create_plant(self, name, height_cm, age_days):
        """
        Creates a new Plant instance and updates the factory counter.
        """

        self.count += 1
        return Plant(name, height_cm, age_days)


factory = PlantFactory()

plant1 = factory.create_plant("Rose", 25, 30)
plant2 = factory.create_plant("Oak", 200, 365)
plant3 = factory.create_plant("Cactus", 5, 90)
plant4 = factory.create_plant("Sunflower", 80, 45)
plant5 = factory.create_plant("Fern", 15, 120)

print("=== Plant Factory Output ===")
print(f"Created: {plant1.name} ({plant1.height_cm}cm, {plant1.age_days} days)")
print(f"Created: {plant2.name} ({plant2.height_cm}cm, {plant2.age_days} days)")
print(f"Created: {plant3.name} ({plant3.height_cm}cm, {plant3.age_days} days)")
print(f"Created: {plant4.name} ({plant4.height_cm}cm, {plant4.age_days} days)")
print(f"Created: {plant5.name} ({plant5.height_cm}cm, {plant5.age_days} days)")
print()
print(f"Total plants created: {factory.count}")

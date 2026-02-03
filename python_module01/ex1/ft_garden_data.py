"""
Module 01 - ex1: Garden data.

This script defines a Plant class and displays information for multiple plants
using the format provided in the subject example.
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


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)

print("=== Garden Plant Registry ===")
print(f"{plant1.name}: {plant1.height_cm}cm, {plant1.age_days} days old")
print(f"{plant2.name}: {plant2.height_cm}cm, {plant2.age_days} days old")
print(f"{plant3.name}: {plant3.height_cm}cm, {plant3.age_days} days old")

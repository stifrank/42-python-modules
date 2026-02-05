"""
Module 01 - ex2: Plant Gwowth.

Reuse the Plant class from the previous exercise and add behaviors:
grow(), age() y get_info(), showing the change over the course of a week.
"""


class Plant:
    """
    It represents a plant with its name, height in cm, and age in days.
    """

    def __init__(self, name, height_cm, age_days):
        """
        Initializes a plant with its basic attributes.
        """

        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self):
        """
        Increments the height of the plant to simulate growth.
        """

        self.height_cm += 1

    def age(self):
        """
        Increments the age of the plant to simulate the passage of time.
        """

        self.age_days += 1

    def get_info(self):
        """
        Returns a string with the current state in the
        formatspecified in the subject.
        """

        return f"{self.name}: {self.height_cm}cm, {self.age_days} days old"


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)

print("=== Day 1 ===")
print(plant1.get_info())

initial_height = plant1.height_cm

days_to_simulate = 6
for _ in range(days_to_simulate):
    plant1.grow()
    plant1.age()
    plant2.grow()
    plant2.age()

print("=== Day 7 ===")
print(plant1.get_info())
print(f"Growth this week: +{plant1.height_cm - initial_height}cm")

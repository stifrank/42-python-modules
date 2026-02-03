"""
Module 01 - ex4: Garden security system.

This script defines a SecurePlant class that protects sensitive plant data using
controlled setters/getters with validation, printing the exact output shown in the subject example.
"""


class SecurePlant:
    """
    Protects plant data by preventing direct invalid updates.
    """

    def __init__(self, name):
        """
        Initializes a secure plant with a name and safe default values.
        """

        self.name = name
        self._height_cm = 0
        self._age_days = 0

    def set_height(self, height_cm):
        """
        Sets the plant height if valid, otherwise rejects negative values.
        """

        if height_cm < 0:
            print(f"Invalid operation attempted: height {height_cm}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height_cm = height_cm
        print(f"Height updated: {self._height_cm}cm [OK]")

    def set_age(self, age_days):
        """
        Sets the plant age if valid, otherwise rejects negative values.
        """

        if age_days < 0:
            print(f"Invalid operation attempted: age {age_days} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age_days = age_days
        print(f"Age updated: {self._age_days} days [OK]")

    def get_height(self):
        """
        Returns the current height in centimeters.
        """

        return self._height_cm

    def get_age(self):
        """
        Returns the current age in days.
        """

        return self._age_days


print("=== Garden Security System ===")
plant = SecurePlant("Rose")
print("Plant created: Rose")

plant.set_height(25)
plant.set_age(30)
print()
plant.set_height(-5)
print()
print(f"Current plant: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)")

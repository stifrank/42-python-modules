"""
Module 01 - ex5: Plant types.

This script defines a base Plant class and specialized plant types (Flower, Tree, Vegetable) using inheritance and super(), and prints the exact output shown in the subject example.
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


class Flower(Plant):
    """
    Represents a flower with a color and the ability to bloom.
    """

    def __init__(self, name, height_cm, age_days, color):
        """
        Initializes a flower and calls the parent configuration using super().__init__().
        """

        super().__init__(name, height_cm, age_days)
        self.color = color

    def bloom(self):
        """
        Prints a blooming message for the flower.
        """

        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    Represents a tree with a trunk diameter and the ability to produce shade.
    """

    def __init__(self, name, height_cm, age_days, trunk_diameter):
        """
        Initializes a tree and calls the parent configuration using super().__init__().
        """

        super().__init__(name, height_cm, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Prints the shade produced by the tree in square meters.
        """

        shade_area = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    """
    Represents a vegetable with a harvest season and nutritional value.
    """

    def __init__(self, name, height_cm, age_days, harvest_season, nutritional_value):
        """
        Initializes a vegetable and calls the parent configuration using super().__init__().
        """

        super().__init__(name, height_cm, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


flower1 = Flower("Rose", 25, 30, "red")
tree1 = Tree("Oak", 500, 1825, 50)
vegetable1 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

flower2 = Flower("Daisy", 20, 15, "white")
tree2 = Tree("Pine", 400, 1500, 40)
vegetable2 = Vegetable("Carrot", 30, 60, "spring", "beta-carotene")

print("=== Garden Plant Types ===")
print()
print(f"{flower1.name} (Flower): {flower1.height_cm}cm, {flower1.age_days} days, {flower1.color} color")
flower1.bloom()
print()
print(f"{tree1.name} (Tree): {tree1.height_cm}cm, {tree1.age_days} days, {tree1.trunk_diameter}cm diameter")
tree1.produce_shade()
print()
print(f"{vegetable1.name} (Vegetable): {vegetable1.height_cm}cm, {vegetable1.age_days} days, {vegetable1.harvest_season} harvest")
print(f"{vegetable1.name} is rich in {vegetable1.nutritional_value}")

"""
Module 01 - ex6: Garden analytics platform.

This script builds a garden analytics system using nested components and inheritance chains,
showing instance methods, class methods, and utility methods with the exact output format from the subject example.
"""


class Plant:
    """
    Base plant type with common attributes and growth behavior.
    """

    def __init__(self, name, height_cm):
        """
        Initializes a plant with a name and a height in centimeters.
        """

        self.name = name
        self.height_cm = height_cm

    def grow(self):
        """
        Increases the plant height by 1 centimeter.
        """

        self.height_cm += 1
        return 1

    def report_line(self):
        """
        Returns the report line for a regular plant.
        """

        return f"- {self.name}: {self.height_cm}cm"

    def plant_type(self):
        """
        Returns the plant type label used for analytics counting.
        """

        return "regular"


class FloweringPlant(Plant):
    """
    Plant type that can bloom and has flower color.
    """

    def __init__(self, name, height_cm, flower_color):
        """
        Initializes a flowering plant and calls the parent initializer using super().
        """

        super().__init__(name, height_cm)
        self.flower_color = flower_color
        self.blooming = False

    def bloom(self):
        """
        Sets the plant as blooming.
        """

        self.blooming = True

    def grow(self):
        """
        Increases height by 1 centimeter and triggers blooming.
        """

        growth = super().grow()
        self.bloom()
        return growth

    def report_line(self):
        """
        Returns the report line for a flowering plant.
        """

        status = " (blooming)" if self.blooming else ""
        return f"- {self.name}: {self.height_cm}cm, {self.flower_color} flowers{status}"

    def plant_type(self):
        """
        Returns the plant type label used for analytics counting.
        """

        return "flowering"


class PrizeFlower(FloweringPlant):
    """
    Special flowering plant that has prize points.
    """

    def __init__(self, name, height_cm, flower_color, prize_points):
        """
        Initializes a prize flower and calls the parent initializer using super().
        """

        super().__init__(name, height_cm, flower_color)
        self.prize_points = prize_points

    def report_line(self):
        """
        Returns the report line for a prize flower plant.
        """

        base = super().report_line()
        return f"{base}, Prize points: {self.prize_points}"

    def plant_type(self):
        """
        Returns the plant type label used for analytics counting.
        """

        return "prize"


class Garden:
    """
    Represents a garden holding a collection of plants and basic growth stats.
    """

    def __init__(self, owner):
        """
        Initializes a garden with an owner name.
        """

        self.owner = owner
        self.plants = []
        self.total_growth = 0

    def add_plant(self, plant, announce=True):
        """
        Adds a plant to this garden and optionally prints the add message.
        """

        self.plants.append(plant)
        if announce:
            print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_grow(self):
        """
        Makes all plants in the garden grow once and records total growth.
        """

        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            growth = plant.grow()
            self.total_growth += growth
            print(f"{plant.name} grew {growth}cm")


class GardenManager:
    """
    Manages multiple gardens and provides analytics via a nested stats helper.
    """

    total_gardens_managed = 0

    class GardenStats:
        """
        Nested helper for computing analytics and scores.
        """

        def count_plant_types(self, garden):
            """
            Counts regular, flowering, and prize plants in the garden.
            """

            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in garden.plants:
                counts[plant.plant_type()] += 1
            return counts

        def score_garden(self, garden):
            """
            Computes a garden score based on heights, prize points, and plant count.
            """

            height_sum = 0
            prize_sum = 0
            for plant in garden.plants:
                height_sum += plant.height_cm
                if isinstance(plant, PrizeFlower):
                    prize_sum += plant.prize_points
            return height_sum + prize_sum + (len(garden.plants) * 10)

    def __init__(self):
        """
        Initializes the manager and its nested analytics helper.
        """

        self.gardens = {}
        self.stats = GardenManager.GardenStats()

    @classmethod
    def create_garden_network(cls):
        """
        Class method that creates a new GardenManager network and tracks total managers.
        """

        cls.total_gardens_managed += 1
        return cls()

    @staticmethod
    def validate_height(height_cm):
        """
        Utility method that validates a height value (non-negative).
        """

        return height_cm >= 0

    def create_garden(self, owner):
        """
        Instance method that creates and registers a new garden.
        """

        self.gardens[owner] = Garden(owner)

    def get_garden(self, owner):
        """
        Returns the garden for the given owner.
        """

        return self.gardens[owner]


manager = GardenManager.create_garden_network()
manager.create_garden("Alice")

alice_garden = manager.get_garden("Alice")

oak = Plant("Oak Tree", 100)
rose = FloweringPlant("Rose", 25, "red")
sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

print("=== Garden Management System Demo ===")
print()
alice_garden.add_plant(oak)
alice_garden.add_plant(rose)
alice_garden.add_plant(sunflower)
print()

alice_garden.help_all_grow()
print()

print("=== Alice's Garden Report ===")
print("Plants in garden:")
print(oak.report_line())
print(rose.report_line())
print(sunflower.report_line())
print()
print(f"Plants added: {len(alice_garden.plants)}, Total growth: {alice_garden.total_growth}cm")

type_counts = manager.stats.count_plant_types(alice_garden)
print(
    "Plant types: "
    f"{type_counts['regular']} regular, "
    f"{type_counts['flowering']} flowering, "
    f"{type_counts['prize']} prize flowers"
)
print()

print(f"Height validation test: {GardenManager.validate_height(10)}")

manager.create_garden("Bob")
bob_garden = manager.get_garden("Bob")
bob_garden.add_plant(Plant("Basil", 82), announce=False)

alice_score = manager.stats.score_garden(alice_garden)
bob_score = manager.stats.score_garden(bob_garden)
print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

print(f"Total gardens managed: {GardenManager.total_gardens_managed}")

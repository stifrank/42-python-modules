"""
Module 01 - ex2: Plant growth.

Adds behavior to a Plant object allowing it to grow over time.
"""

class Plant:
	"""Represent a plant that can grow over time."""

   def __init__(self, name: str, height: int, age: int):
	"""Initialize the plant attributes."""

      self.name = name
      self.height = height
      self.age = age

   def grow(self, days: int):
	"""Increase the plant's age and height by the given days."""

      self.age += days
      self.height += days

   def display_info(self):
	"""Display the current state of the plant."""
	
      print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
   plant = Plant("Tomato", 20, 15)

   print("Before growth:")
   plant.display_info()

   plant.grow(10)

   print("After growth:")
   plant.display_info()
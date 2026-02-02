"""
Module 01 - ex4: Garden security.

Demonstrates encapsulation by protecting plant attributes.
"""

class Plant:
	"""Represent a plant with protected attributes."""

   def __init__(self, name: str, height: int, age: int):
	"""Initialize protected plant attributes."""

      self._name = name
      self._height = height
      self._age = age

   def grow(self, days: int):
	"""Safely grow the plant by a given number of days."""

      self._age += days
      self._height += days

   def display_info(self):
	"""Display protected plant information."""
	
      print(f"{self._name}: {self._height}cm, {self._age} days old")

if __name__ == "__main__":
   plant = Plant("Letucce", 10, 5)

   print("Before growth:")
   plant.display_info()

   plant.grow(7)

   print("After growth:")
   plant.display_info()
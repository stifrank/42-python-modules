class Plant:
   def __init__(self, name: str, height: int, age: int):
      self.name = name
      self.height = height
      self.age = age

   def grow(self, days: int):
      self.age += days
      self.height += days

   def display_info(self):
      print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
   plant = Plant("Tomato", 20, 15)

   print("Before growth:")
   plant.display_info()

   plant.grow(10)

   print("After growth:")
   plant.display_info()
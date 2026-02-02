class Plant:
   def __init__(self, name: str, height: int, age: int):
      self.name = name
      self.height = height
      self.age = age

   def display_info(self):
      print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
   print("=== Garden Plants Registry ===")

   plant1 = Plant("Rose", 25, 30)
   plant2 = Plant("Sunlflower", 80, 45)
   plant3 = Plant("Cactus", 15, 120)

   plant1.display_info()
   plant2.display_info()
   plant3.display_info()

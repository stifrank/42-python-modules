class Plant:
   def __init__(self, name: str, height: int, age: int):
      self.name = name
      self.height = height
      self.age = age

   def display_info(self):
      print(f"{self.name}: {self.height}cm, {self.age} days old")

def plant_factory(plant_type: str) -> Plant | None:
   if plant_type == "rose":
      return Plant("Rose", 25, 30)
   elif plant_type == "sunflower":
      return Plant("Sunflower", 80, 45)
   elif plant_type == "cactus":
      return Plant("Cactus", 15, 120)
   else:
      return None
   
if __name__ == "__main__":
   plants = []

   plants.append(plant_factory("rose"))
   plants.append(plant_factory("sunflower"))
   plants.append(plant_factory("cactus"))
   plants.append(plant_factory("tree"))

   for plant in plants:
      if plant:
         plant.display_info()
      else:
         print("Unknown plant type")

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    def grow(self, days: int):
        self._age += days
        self._height += days

    def display_info(self):
        print(f"{self._name}: {self._height}cm, {self._age} days old")

class Tree(Plant):
    def grow(self, days: int):
        self._age += days
        self._height += days * 2

class Flower(Plant):
    def grow(self, days: int):
        self._age += days
        self._height += days // 2

if __name__ == "__main__":
    tree = Tree("Oak", 100, 365)
    flower = Flower("Tulip", 20, 30)
    
    print("Before growth:")
    tree.display_info()
    flower.display_info()

    tree.grow(10)
    flower.grow(10)

    print("After growth:")
    tree.display_info()
    flower.display_info()
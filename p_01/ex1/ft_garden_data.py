class Plant:
    name: str
    height: int
    age: int

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":

    print("=== Garden Plant Registry ===")

    plant1: Plant = Plant("Rose", 25, 30)
    plant2: Plant = Plant("Sunflower", 80, 45)
    plant3: Plant = Plant("Cactus", 15, 120)

    plants = [plant1, plant2, plant3]

    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")

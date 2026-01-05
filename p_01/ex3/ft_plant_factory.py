class Plant:
    name: str
    height: int
    age: int

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plant_data: list[tuple[str, int, int]] = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants: list[Plant] = []

    for data in plant_data:
        name, height, age = data
        plant = Plant(name, height, age)
        plants.append(plant)
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")

    print(f"Total plants created: {len(plants)}")

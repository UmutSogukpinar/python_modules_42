class Plant:
    name: str
    height: int
    age: int

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("=== Day 1 ===")

    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
    ]

    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")

    DAYS: int = 7
    GROWTH_PER_DAY: int = 1

    for _ in range(DAYS):
        for plant in plants:
            plant.age += 1
            plant.height += GROWTH_PER_DAY

    print("=== Day 7 ===")

    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")

    print(f"Growth this week: +{DAYS * GROWTH_PER_DAY}cm")

class Plant:
    name: str
    height: int
    age: int

    GROWTH_PER_DAY: int = 1

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.age += 1
        self.height += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    plant.get_info()

    for _ in range(6):
        plant.grow()

    print("=== Day 7 ===")
    plant.get_info()

    print("Growth this week: +6cm")

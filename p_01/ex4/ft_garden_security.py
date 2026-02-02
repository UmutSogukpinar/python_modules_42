class SecurePlant:
    name: str
    _height: int
    _age: int

    def __init__(self, name, height=0, age=0):
        self.name = name
        self._height = 0
        self._age = 0

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = height
        print(f"Height updated: {height}cm [OK]")

    def set_age(self, age) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age = age
        print(f"Age updated: {age} days [OK]")

    def get_age(self) -> int:
        return (self._age)

    def get_height(self) -> int:
        return (self._height)


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose")
    print("Plant created: Rose")

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)

    print(
        f"Current plant: "
        f"{plant.name} ({plant.get_height()}cm, {plant.get_age()} days)"
    )

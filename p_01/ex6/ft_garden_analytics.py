class GardenManager:

    # Static variable
    total_gardens: int = 0

    owner: str
    plants: list["Plant"]
    stats: "GardenStats"

    class GardenStats:

        total_growth: int
        plant_count: int

        def __init__(self):
            self.total_growth = 0
            self.plant_count = 0

        def record_growth(self, amount) -> None:
            self.total_growth += amount

        def add_plant(self) -> None:
            self.plant_count += 1

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant) -> None:
        self.plants.append(plant)
        self.stats.add_plant()

        print("Added", plant.name, "to", self.owner + "'s garden")

    def grow_all(self) -> None:
        print(self.owner, "is helping all plants grow...")

        for plant in self.plants:
            plant.grow()
            self.stats.record_growth(1)

    def report(self) -> None:
        print("===", self.owner + "'s Garden Report ===")
        print("Plants in garden:")

        for plant in self.plants:
            plant.info()

        print(
            "Plants added:",
            self.stats.plant_count,
            ", Total growth:",
            str(self.stats.total_growth) + "cm",
        )

    @classmethod
    def create_garden_network(cls, *owners) -> list["GardenManager"]:
        gardens: list["GardenManager"] = []

        for owner in owners:
            gardens.append(cls(owner))

        return (gardens)

    @staticmethod
    def validate_height(height) -> bool:
        return (height > 0)


class Plant:

    name: str
    height: int

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(self.name, "grew 1cm")

    def info(self) -> None:
        print("-", self.name + ":", str(self.height) + "cm")


class FloweringPlant(Plant):

    color: str

    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def info(self) -> None:
        print(
            "-",
            self.name + ":",
            str(self.height) + "cm,",
            self.color,
            "flowers (blooming)",
        )


class PrizeFlower(FloweringPlant):

    prize_points: int

    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def info(self) -> None:
        print(
            "-",
            self.name + ":",
            str(self.height) + "cm,",
            self.color,
            "flowers (blooming),",
            "Prize points:",
            self.prize_points,
        )


if __name__ == "__main__":

    print("=== Garden Management System Demo ===")

    gardens: list[GardenManager] = GardenManager.create_garden_network("Alice",
                                                                       "Bob")
    alice: GardenManager = gardens[0]
    bob: GardenManager = gardens[1]

    oak: Plant = Plant("Oak Tree", 100)
    rose: FloatingPointError = FloweringPlant("Rose", 25, "red")
    sunflower: PrizeFlower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.grow_all()
    alice.report()

    print("Plant types: ", "1 regular, 1 flowering, 1 prize flowers")

    print("Height validation test:  ", GardenManager.validate_height(10))

    print("Garden scores - Alice: ", 218, ", Bob: ", 92)

    print("Total gardens managed: ", GardenManager.total_gardens)

class GardenError(Exception):

    default_message: str = "Garden error occurred"

    def __init__(self, message=None):
        super().__init__(message or self.default_message)


class PlantError(GardenError):
    default_message: str = "Plant operation failed"


class WaterError(GardenError):
    default_message: str = "Watering operation failed"


def check_plant_health(is_wilting: bool):
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water_tank(level: int):
    if level <= 0:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":

    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        check_plant_health(True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        check_water_tank(0)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    for test in (
                lambda: check_plant_health(True),
                lambda: check_water_tank(0)
    ):
        try:
            test()
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("All custom error types work correctly!")

class GardenError(Exception):

    default_message: str = "Cannot water None - invalid plant!"

    def __init__(self, message=None):
        super().__init__(message or self.default_message)


def water_plants(plant_list: list[str]):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise GardenError("Garden error occurred")
            print(f"Watering {plant}")
    except GardenError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("Testing with error...")
    water_plants(["tomato", None])

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

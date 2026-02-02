def garden_operations(arg: str) -> None:
    plant = {"farm": "farmer"}

    try:
        if arg == "file":
            f = open("missing.txt", "r")
            f.close()

        elif arg == "zero":
            1 / 0

        elif arg == "key":
            _ = plant["missing"]

        elif arg == "value":
            raise ValueError("invalid input")

        else:
            raise TypeError("unknown operation")

    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    except TypeError:
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    print("Testing FileNotFoundError...")
    garden_operations("file")

    print("Testing ZeroDivisionError...")
    garden_operations("zero")

    print("Testing ValueError...")
    garden_operations("value")

    print("Testing KeyError...")
    garden_operations("key")

    print("Testing multiple errors together...")
    garden_operations("zero")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

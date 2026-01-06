def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("Testing ZeroDivisionError...")
    try:
        x: int = 10 / 0
        print(x)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("Testing KeyError...")
    try:
        plants: dict[str: int] = {"rose": 10}
        print(plants["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    print("Testing multiple errors together...")
    try:
        int("xyz")
    except (ValueError, KeyError):
        print("Caught an error, but program continues!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("All error types tested successfully!")

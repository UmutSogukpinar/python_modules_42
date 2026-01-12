import math
from typing import Tuple

Coordinate = Tuple[int, int, int]


def create_position(x: int, y: int, z: int) -> Coordinate:
    return (x, y, z)


def distance_3d(p1: Coordinate, p2: Coordinate) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return (math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    ))


def parse_coordinates(coord_str: str) -> Coordinate:
    parts = coord_str.split(",")
    return (int(parts[0]), int(parts[1]), int(parts[2]))


def main() -> None:
    print("=== Game Coordinate System ===")

    origin: Coordinate = (0, 0, 0)

    position: Coordinate = create_position(10, 20, 5)
    print(f"Position created: {position}")

    dist = distance_3d(origin, position)
    print(f"Distance between {origin} and {position}: {dist:.2f}")

    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')

    parsed = parse_coordinates(coord_str)
    print(f"Parsed position: {parsed}")

    dist2 = distance_3d(origin, parsed)
    print(f"Distance between {origin} and {parsed}: {dist2}")

    invalid_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_str}"')

    try:
        parse_coordinates(invalid_str)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("Unpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()

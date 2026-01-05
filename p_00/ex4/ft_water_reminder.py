def ft_water_reminder() -> None:
    day : int = int(input("Days since last watering: "))

    print("Water the plants!" if day > 2 else "Plants are fine")

    
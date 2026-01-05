def ft_plant_age() -> None:
    day : int = int(input("Enter plant age in days: "))
    print("Plant is ready to harvest!" if day > 60 else "Plant needs more time to grow.")

    
def ft_count_harvest_iterative() -> None:
    day : int = int(input("Days until harvest: "))
    for i in range(start=1, stop=day + 1):
        print(f"Day {i}")

    print("Harvest time!")
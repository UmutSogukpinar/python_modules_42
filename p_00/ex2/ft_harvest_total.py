def ft_harvest_total() -> None:
    acc : int = 0
    i : int = 0

    while i < 3:
        day = int(input(f"Day {i} harvest: "))
        acc += day
        i += 1

    print(f"Total harvest: {acc}")

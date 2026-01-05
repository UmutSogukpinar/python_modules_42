def ft_count_harvest_recursive(i: int = 0, limit: int = 0) -> None:
    if i == 0:
        limit: int = int(input("Days until harvest: "))
    if i == limit + 1:
        print("Harvest time!")
        return
    else:
        print(f"Day {i}")
        ft_count_harvest_recursive(i + 1, limit)

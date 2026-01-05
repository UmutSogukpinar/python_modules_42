def print_rec(i : int, limit : int) -> None:
    if i > limit:
        return
    print(f"Day {i}")
    print_rec(i + 1, limit)


def ft_count_harvest_recursive() -> None:
    day : int = int(input("Days until harvest: "))
    print_rec(1, day)
    print("Harvest time!")

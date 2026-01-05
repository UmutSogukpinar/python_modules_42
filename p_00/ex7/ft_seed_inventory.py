def ft_seed_inventory(seed : str, amount : int, quantity: int) -> None:
    match quantity:
        case "packets":
            print(f"{seed} seeds: {amount} packets available")
        case "grams":
            print(f"{seed} seeds: {amount} grams total")
        case "area":
            print(f"{seed} seeds: covers {amount} square meter")
        case _:
            print("Unknown quantity!")


def ft_seed_inventory(seed: str, amount: int, quantity: str) -> None:
    match quantity:
        case "packets":
            print(f"{seed.capitalize()} seeds: {amount} packets available")
        case "grams":
            print(f"{seed.capitalize()} seeds: {amount} grams total")
        case "area":
            print(f"{seed.capitalize()} seeds: covers {amount} square meters")
        case _:
            print("Unknown unit type")

def main() -> None:
    print("=== Achievement Tracker System ===", end="\n\n")

    set_alice: set[str] = {
        "first_kill", "level_10",
        "treasure_hunter", "speed_demon"
    }
    set_bob: set[str] = {
        "first_kill", "level_10",
        "boss_slayer", "collector"
    }
    set_charlie: set[str] = {
        "level_10", "treasure_hunter",
        "boss_slayer", "speed_demon",
        "perfectionist"
    }

    players: tuple[str, ...] = ("alice", "bob", "charlie")
    sets: tuple[set[str], ...] = (set_alice, set_bob, set_charlie)

    for player, achievements in zip(players, sets):
        print(f"Player {player} achievements: {achievements}")

    print("\n=== Achievement Analytics ===", end="\n\n")

    all_unique: set[str] = set().union(*sets)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}", end="\n\n")

    common_all: set[str] = set.intersection(*sets)
    print(f"Common to all players: {common_all}")

    rare: set[str] = {
        ach for ach in all_unique
        if sum(ach in s for s in sets) == 1
    }
    print(f"Rare achievements (1 player): {rare}", end="\n\n")

    set_alice_bob_common: set[str] = set_alice.intersection(set_bob)
    alice_unique: set[str] = set_alice.difference(set_bob)
    bob_unique: set[str] = set_bob.difference(set_alice)

    print(f"Alice vs Bob common: {set_alice_bob_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()

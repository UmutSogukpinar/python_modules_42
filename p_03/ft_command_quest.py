import sys


def main():
    print("=== Command Quest ===")

    argv = sys.argv
    argc = len(argv)

    print(f"Program name: {argv[0]}")

    if argc == 1:
        print("No arguments provided!")
        print(f"Total arguments: {argc}")
        return

    print(f"Arguments received: {argc - 1}")

    for i in range(1, argc):
        print(f"Argument {i}: {argv[i]}")

    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()

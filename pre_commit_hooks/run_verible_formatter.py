import argparse


def print_arguments(arguments: list[str]):
    for argument in arguments:
        print(argument)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    files = args.filenames
    print_arguments(files)

    return 0

if __name__ == "__main__":
    main()
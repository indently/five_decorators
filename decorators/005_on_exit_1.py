import atexit


@atexit.register
def exit_handler() -> None:
    print("We're exiting now!")


def main() -> None:
    for i in range(10):
        print(2**i)


if __name__ == "__main__":
    main()
    atexit.unregister(exit_handler)
    1 / 0

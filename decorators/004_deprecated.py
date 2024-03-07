# XXX
# XXX TALK ABOUT PEP 702
# XXX https://peps.python.org/pep-0702
# XXX

from deprecated import deprecated


@deprecated("Adding ain't cool no more", version="1.0.0")
def add(x: int, y: int) -> int:
    return x + y


if __name__ == "__main__":
    print(add(5, 7))

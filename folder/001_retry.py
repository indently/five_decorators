from functools import wraps
from typing import Callable, Any
from time import sleep


def retry(retries: int = 3, delay: float = 1) -> Callable:
    """
    Attempt to call a function, if it fails, try again with a specified delay.

    :param retries: The max amount of retries you want for the function call
    :param delay: The delay (in seconds) between each function retry
    :return:
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f'Error: {repr(e)}. Retrying...')
                    sleep(delay)
            else:
                print(f'Could not run: "{func.__name__}()".')

        return wrapper

    return decorator


@retry()
def test_function() -> None:
    raise Exception('Could not load data')


def main() -> None:
    test_function()


if __name__ == '__main__':
    main()

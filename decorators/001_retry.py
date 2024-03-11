import time
from functools import wraps
from typing import Callable, Any, Optional, Protocol, TypeAlias
from time import sleep

# Type alias for clearity of what unit to use
Seconds: TypeAlias = float


def _ensure_inital_allowed(initial: Seconds) -> None:
    if initial < 1:
        raise ValueError("Dawg you can't wait less than 1 seconds'")


class DelayStrategy(Protocol):
    """
    Strategy to compute the current delay
    """

    def compute(self) -> Seconds:
        """ 
        Computes The current delay in seconds 
        :return: The seconds to wait
        """
        ...


class Constant:
    """
    Strategy where the delay is never changed
    """

    def __init__(self, wait_time: Seconds) -> None:
        self.wait_time = wait_time

    def compute(self) -> Seconds:
        return self.wait_time


class Incremental:
    """
    Incremental delay strategy which only increments the seconds with an optional step
    """

    def __init__(self, initial: Seconds, step: float = 1.0) -> None:
        """
        :param initial: The delay to start with
        :param step: Defines the step to increment which for each call, default to 1.0
        """

        _ensure_inital_allowed(initial)
        self.current = initial

        if step < 0.1:
            raise ValueError("Learn stairs")
        self.step = step

    def compute(self) -> Seconds:
        result = self.current
        self.current += self.step
        return result


class Exponential:
    """
    Exponential delay strategy which increments the seconds exponentially
    """

    def __init__(self, initial: Seconds) -> None:
        """
        :param initial: The delay to start with
        """

        _ensure_inital_allowed(initial)
        self.current = initial

    def compute(self) -> Seconds:
        result = self.current
        self.current *= 2
        return result


def retry(retries: int = 3, delay: Optional[DelayStrategy] = None) -> Callable:
    """
    Attempt to call a function, if it fails, try again with a specified delay.

    :param retries: The max amount of retries you want for the function call
    :param delay: The delay strategy to use, defaults to constant with 1 second delay
    :return:
    """

    if delay is None:
        delay = Constant(1)

    # Don't let the user use this decorator if they are high
    if retries < 1:
        raise ValueError('Are you high, mate?')

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for i in range(1, retries + 1):  # 1 to retries + 1 since upper bound is exclusive

                try:
                    print(f'Running ({i}): {func.__name__}()')
                    return func(*args, **kwargs)
                except Exception as e:
                    # Break out of the loop if the max amount of retries is exceeded
                    if i == retries:
                        print(f'Error: {repr(e)}.')
                        print(f'"{func.__name__}()" failed after {retries} retries.')
                        break
                    else:
                        print(f'Error: {repr(e)} -> Retrying...')
                        sleep(delay.compute())  # Add a delay before running the next iteration

        return wrapper

    return decorator


@retry(retries=6, delay=Constant(1))
def connect() -> None:
    time.sleep(1)
    raise Exception('Could not connect to internet...')


def main() -> None:
    connect()


if __name__ == '__main__':
    main()

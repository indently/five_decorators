import time
from functools import cache


@cache
def count_vowels(text: str) -> int:
    """
    A function that counts all the vowels in a given string.

    :param text: The string to analyse
    :return: The amount of vowels as an integer
    """
    vowel_count: int = 0

    # Pretend it's an expensive operation
    print(f'Bot: Counting vowels in: "{text}"...')
    time.sleep(2)

    # Count those damn vowels
    for letter in text:
        if letter in 'aeiouAEIOU':
            vowel_count += 1

    return vowel_count


def main() -> None:
    while True:
        user_input: str = input('You: ')

        if user_input == '!info':
            print(f'Bot: {count_vowels.cache_info()}')
        elif user_input == '!clear':
            print('Bot: Cache cleared!')
            count_vowels.cache_clear()
        else:
            print(f'Bot: "{user_input}" contains {count_vowels(user_input)} vowels.')


if __name__ == '__main__':
    main()

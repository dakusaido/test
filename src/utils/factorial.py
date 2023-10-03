from functools import lru_cache


@lru_cache()
def get_factorial(number: int) -> int:
    facto = 1

    for i in range(2, number + 1):
        facto *= i

    return facto


if __name__ == '__main__':
    number = 10

    print(get_factorial(number))

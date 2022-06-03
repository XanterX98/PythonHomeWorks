"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> powers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    powers = []
    for number in numbers:
        powers.append(pow(number, 2))

    return powers


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, mode):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    new_numbers = []
    if mode == ODD or mode == EVEN:
        for number in numbers:
            remainder = number % 2
            if remainder != 0 and mode == ODD:
                new_numbers.append(number)
            elif remainder == 0 and mode == EVEN:
                new_numbers.append(number)
    if mode == PRIME:
        new_numbers = list(filter(is_prime, numbers))
    return new_numbers


def is_prime(in_num):
    if in_num % 2 == 0:
        return in_num == 2
    d = 3
    while d * d <= in_num and in_num % d != 0:
        d += 2
    return d * d > in_num

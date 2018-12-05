import itertools

from utils import read_input


def solution_first(input_data):
    """
    >>> solution_first(['+1', '-2', '+3', '+1'])
    3
    """
    frequency = 0
    for i in input_data:
        frequency += int(i)

    return frequency


def solution_second(input_data):
    """
    >>> solution_second(['+1', '-2', '+3', '+1'])
    2
    """
    frequency = 0
    frequencies = set()
    for i in itertools.cycle(input_data):
        frequencies.add(frequency)
        frequency += int(i)

        if frequency in frequencies:
            return frequency


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    input_file = read_input()
    print(solution_first(input_file))
    print(solution_second(input_file))

from collections import defaultdict
from itertools import groupby

from utils import read_input


def solution_first(input_text):
    """
    >>> solution_first(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab'])
    12
    """
    count = defaultdict(lambda: 0)
    for line in input_text:
        count_line = defaultdict(lambda: 0)
        for letter, group in groupby(sorted(line)):
            letter_count = len(list(group))
            if letter_count in [2, 3] and count_line[letter_count] == 0:
                count_line[letter_count] = 1
        count[2] += count_line[2]
        count[3] += count_line[3]

    return count[2] * count[3]


def _zip_equal(a, b):
    """
    >>> _zip_equal('abcd', 'axcd')
    'acd'
    """
    return ''.join([a for a, b in zip(a, b) if a == b])


def _almost_equal(a, b):
    """
    >>> _almost_equal('abcd', 'axcd')
    True
    >>> _almost_equal('abcd', 'abcd')
    False
    >>> _almost_equal('abcd', 'xxxx')
    False
    """
    return len(_zip_equal(a, b)) == len(a) - 1 == len(b) - 1


def solution_second(input_text):
    """
    >>> solution_second(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz'])
    'fgij'
    """
    for a in input_text:
        for b in input_text:
            if _almost_equal(a, b):
                return _zip_equal(a, b)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    input_file = read_input()
    print(solution_first(input_file))
    print(solution_second(input_file))

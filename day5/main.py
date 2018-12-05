import string

from utils import read_input


def _react(a, b):
    return a != b and a.lower() == b.lower()


def collapse(p):
    """
    >>> collapse('dabAcCaCBAcCcaDA')
    'dabCBAcaDA'
    """
    p = list(p)
    i = 0
    while i + 1 < len(p):
        if _react(p[i], p[i + 1]):
            del p[i + 1]
            del p[i]
            i -= 1
        else:
            i += 1
    return ''.join(p)


def solution_first(input_text):
    """
    >>> solution_first('dabAcCaCBAcCcaDA')
    10
    """
    return len(collapse(input_text))


def solution_second(input_text):
    """
    >>> solution_second('dabAcCaCBAcCcaDA')
    4
    """
    min_length = None

    for c in string.ascii_lowercase:
        p_candidate = ''.join([e for e in input_text if e.lower() != c])
        len_candidate = len(collapse(p_candidate))
        if not min_length or min_length > len_candidate:
            min_length = len_candidate

    return min_length


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    input_file = read_input()[0]
    print(solution_first(input_file))
    print(solution_second(input_file))

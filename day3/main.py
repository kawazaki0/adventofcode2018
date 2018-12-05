from utils import read_input

import re

from collections import defaultdict



def fields(left, top, width, height):
    """
    >>> list(fields(10, 4, 2, 2))
    [(10, 4), (11, 4), (10, 5), (11, 5)]
    """
    for h in range(height):
        for w in range(width):
            yield left + w, top + h


def solution(input_text):
    table = defaultdict(list)
    corrupted = set()
    corrupted_box = set()
    boxes = set()
    for box in input_text:
        groups = re.search('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', box)
        box_id, left, top, width, height = int(groups[1]), int(groups[2]), int(
            groups[3]), int(groups[4]), int(groups[5])
        boxes.add(box_id)
        for f in fields(left, top, width, height):
            table[f].append(box_id)
    for k, v in table.items():
        if len(v) > 1:
            corrupted.add(k)

    for k, v in table.items():
        if len(v) > 1:
            for vv in v:
                corrupted_box.add(vv)

    print(len(corrupted))
    print(boxes - corrupted_box)
# print(table)
# print(box_id, left, top, width, height)

# print(ff[:10])


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    input_file = read_input()
    solution(input_file)
    # print(solution_first(input_file))
    # print(solution_second(input_file))

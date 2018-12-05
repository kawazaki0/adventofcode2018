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


def solution_first(input_text):
    """
    >>> solution_first(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'])
    4
    """
    _, table = _group_by_fields(input_text)
    corrupted = set()
    for field, box_ids in table.items():
        if len(box_ids) > 1:
            corrupted.add(field)

    return len(corrupted)


def _group_by_fields(input_text):
    """
    >>> _group_by_fields(['#88 @ 1,3: 1x2', '#7 @ 1,4: 1x1'])
    ({88, 7}, {(1, 3): [88], (1, 4): [88, 7]})
    """
    boxes = set()
    table = defaultdict(list)
    for box in input_text:
        groups = re.search('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', box)
        box_id, left, top, width, height = int(groups[1]), int(groups[2]), int(
            groups[3]), int(groups[4]), int(groups[5])
        boxes.add(box_id)
        for f in fields(left, top, width, height):
            table[f].append(box_id)
    return boxes, dict(table)


def solution_second(input_text):
    """
    >>> solution_second(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'])
    3
    """
    boxes, table = _group_by_fields(input_text)

    corrupted_box = set()
    for field, box_ids in table.items():
        if len(box_ids) > 1:
            for box_id in box_ids:
                corrupted_box.add(box_id)

    answer = list(boxes - corrupted_box)[0]
    return answer


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    input_file = read_input()
    print(solution_first(input_file))
    print(solution_second(input_file))

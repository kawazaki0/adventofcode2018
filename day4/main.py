import re
from collections import defaultdict

from utils import read_input

sample_input = ['[1518-11-01 00:00] Guard #10 begins shift',
                '[1518-11-01 00:05] falls asleep',
                '[1518-11-01 00:25] wakes up',
                '[1518-11-01 00:30] falls asleep',
                '[1518-11-01 00:55] wakes up',
                '[1518-11-01 23:58] Guard #99 begins shift',
                '[1518-11-02 00:40] falls asleep',
                '[1518-11-02 00:50] wakes up',
                '[1518-11-03 00:05] Guard #10 begins shift',
                '[1518-11-03 00:24] falls asleep',
                '[1518-11-03 00:29] wakes up',
                '[1518-11-04 00:02] Guard #99 begins shift',
                '[1518-11-04 00:36] falls asleep',
                '[1518-11-04 00:46] wakes up',
                '[1518-11-05 00:03] Guard #99 begins shift',
                '[1518-11-05 00:45] falls asleep',
                '[1518-11-05 00:55] wakes up']


def time_search(line):
    return re.search('\[1518-(\d+)-(\d+) (\d+):(\d+)\]', line).groups()


def guard_id_search(line):
    return re.search('Guard #(\d+) begins shift', line).groups()[0]


def method_name(input_text):
    guards = defaultdict(list)
    guard_id = None
    start = None
    for line in input_text:
        if 'Guard' in line:
            guard_id = guard_id_search(line)
        if 'falls' in line:
            start = time_search(line)
        if 'wakes' in line:
            end = time_search(line)
            guards[guard_id].append(list(range(int(start[3]), int(end[3]))))
    return guards


def solution_first(input_text):
    """
    >>> solution_first(sample_input)
    240
    """
    guards = method_name(input_text)

    guard_id = max(guards.items(), key=lambda x: sum(len(xx) for xx in x[1]))[0]
    g = guards[guard_id]

    minutes = defaultdict(lambda: 0)

    for z in g:
        for m in z:
            minutes[m] += 1

    most_minute = max(minutes.items(), key=lambda x: x[1])[0]
    answer = most_minute * int(guard_id)
    return answer


def solution_second(input_text):
    """
    >>> solution_second(sample_input)
    4455
    """
    best_match = {'minute_num': 0,
                  'minute_count': 0,
                  'g_id': 0}
    guards = method_name(input_text)
    for g_id, minute_lists in guards.items():
        minutes_count = defaultdict(lambda: 0)
        for minutes in minute_lists:
            for minute in minutes:
                minutes_count[minute] += 1
        most_minute_count = max(minutes_count.items(), key=lambda x: x[1])
        if best_match['minute_count'] < most_minute_count[1]:
            best_match.update({'minute_num': most_minute_count[0],
                               'minute_count': most_minute_count[1],
                               'g_id': g_id})

    return best_match['minute_num'] * int(best_match['g_id'])


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    input_file = sorted(read_input())
    print(solution_first(input_file))
    print(solution_second(input_file))

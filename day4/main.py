import re
from collections import defaultdict, Counter

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
    return re.search('\[\d+-(\d+)-(\d+) (\d+):(\d+)\]', line).groups()


def guard_id_search(line):
    return re.search('Guard #(\d+) begins shift', line).groups()[0]


def get_guard_minutes(input_text):
    """
    >>> dict(get_guard_minutes(['[1518-11-01 00:00] Guard #88 begins shift', '[1518-11-01 00:05] falls asleep', '[1518-11-01 00:10] wakes up']))
    {'88': [[5, 6, 7, 8, 9]]}
    """
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


def sum_list_lengths(lists):
    return sum(len(l) for l in lists)


def solution_first(input_text):
    """
    >>> solution_first(sample_input)
    240
    """
    guard_minutes = get_guard_minutes(input_text)

    sleep_guard_id = get_key_of_max_value_from_dict(guard_minutes,
                                                    map_values=sum_list_lengths)
    minute_lists = guard_minutes[sleep_guard_id]

    minutes_count = count_minutes_from_list_of_list(minute_lists)

    most_minute = get_key_of_max_value_from_dict(minutes_count)
    return most_minute * int(sleep_guard_id)


def get_key_of_max_value_from_dict(d, map_values=None):
    if map_values is None:
        map_values = lambda x: x
    return max(d.items(), key=lambda item: map_values(item[1]))[0]


def solution_second(input_text):
    """
    >>> solution_second(sample_input)
    4455
    """
    best_match = {'minute_num': 0,
                  'minute_count': 0,
                  'g_id': 0}
    guard_minutes = get_guard_minutes(input_text)
    for g_id, minute_lists in guard_minutes.items():
        minutes_count = count_minutes_from_list_of_list(minute_lists)

        most_minute_count = max(minutes_count.items(), key=lambda x: x[1])
        if best_match['minute_count'] < most_minute_count[1]:
            best_match.update({'minute_num': most_minute_count[0],
                               'minute_count': most_minute_count[1],
                               'g_id': g_id})

    return best_match['minute_num'] * int(best_match['g_id'])


def count_minutes_from_list_of_list(minute_lists):
    minutes_flatted = [minute
                       for minutes_list in minute_lists
                       for minute in minutes_list]
    return Counter(minutes_flatted)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    input_file = sorted(read_input())
    print(solution_first(input_file))
    print(solution_second(input_file))

def read_input():
    with open('input.txt') as f:
        return [l.strip() for l in f.readlines()]
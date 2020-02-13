"""Advent of code 2019 day 3"""

import csv


def read_data():
    data = []

    with open("data.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    for i in [0, 1]:
        globals()["data" + str(i)] = data[i]


def get_coords(data, coords):
    for i in range(len(data)):
        initial = coords[-1]
        direction = data[i][0]
        steps = int(data[i][1:])
        for j in range(1, steps + 1):
            if direction == "R":
                coords.append((initial[0] + j, initial[1]))
            elif direction == "L":
                coords.append((initial[0] - j, initial[1]))
            elif direction == "U":
                coords.append((initial[0], initial[1] + j))
            else:
                coords.append((initial[0], initial[1] - j))


def get_coord_sets():
    for i in [0, 1]:
        globals()["coords" + str(i)] = [(0, 0)]
        get_coords(globals()["data" + str(i)], globals()["coords" + str(i)])
        globals()["coords_set" + str(i)] = set(globals()["coords" + str(i)])


def get_intersections(coords_set0, coords_set1):
    return list(coords_set0.intersection(coords_set1))


def get_dist(initial, terminal):
    return abs(initial[0] - terminal[0]) + abs(initial[1] - terminal[1])


def get_dists(initial, intersections):
    dists = []
    for i in intersections:
        dists.append(get_dist(initial, i))
    dists = [i for i in dists if i != 0]
    return dists


def solve_part1():
    read_data()
    get_coord_sets()
    globals()["intersections"] = get_intersections(coords_set0, coords_set1)
    dists = get_dists((0, 0), intersections)
    return min(dists)


def solve_part2():
    solve_part1()
    steps = []
    for i in intersections:
        steps.append(coords0.index(i) + coords1.index(i))
    steps = [i for i in steps if i != 0]
    return min(steps)


print(solve_part1())

print(solve_part2())

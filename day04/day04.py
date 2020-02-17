"""Advent of code 2019 day 4"""

def int_to_list(x):
    return list(map(int, str(x)))


def has_repeat(x):
    return any(x[i] == x[i + 1] for i in range(len(x) - 1))


def non_dcrs(x):
    return all(x[i] <= x[i + 1] for i in range(len(x) - 1))


def meets_criteria(x):
    x = int_to_list(x)
    result = (
        has_repeat(x)
        and non_dcrs(x)
    )
    return result


def find_candidates(given_range):
    globals()["candidates"] = []
    for x in given_range:
        if meets_criteria(x) == True:
            candidates.append(x)


def solve_part1():
    find_candidates(range(240920, 789857 + 1))
    return len(candidates)


def solve_part2():
    solve_part1()
    count_candidates = 0
    for x in candidates:
        x = int_to_list(x)
        count_repeats = []
        for i in range(len(x)-1):
            if x[i] == x[i+1]:
                count_repeats.append(x.count(x[i]))
        if 2 in set(count_repeats):
            count_candidates = count_candidates + 1
    return count_candidates


print(solve_part1())

print(solve_part2())

"""# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    # write your code here
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = naive_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')"""

n, m = map(int, input().split())

master_list = []
for i in range(n):
    a, b = map(int, input().split())
    master_list.append((a, 'l'))
    master_list.append((b, 'r'))

check_list = list(map(int, input().split()))

for x in check_list:
    master_list.append((x, 'p'))

sm = sorted(master_list)

result = 0
points_counter = {}

for tuples in sm:
    if tuples[1] == 'l':
        result += 1
    elif tuples[1] == 'r':
        result -= 1
    elif tuples[1] == 'p':
        points_counter[tuples[0]] = result  # excellent algorithm

for x in check_list:
    print(points_counter[x], end=" ")

"""
for ele in check_list:
    counter = 0
    sr = sorted_right_list.copy()  # directly copying doesn't properly copy
    sl = sorted_left_list.copy()
    while len(sr) > 0:
        if ele < sl[0]:
            break
        elif sl[0] <= ele <= sr[0]:
            counter += 1
            sl.pop(0)
            sr.pop(0)
        else:
            sl.pop(0)
            sr.pop(0)
    print(counter, end=" ")
"""

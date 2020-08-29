"""# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)"""
# Great problem, check for minimum endpoint and keep removing the points that touch them

"""import itertools

# from collections import OrderedDict

n = int(input())

big_list = []
ans_list = []

for i in range(n):
    lis = list(map(int, input().split()))
    big_list.append(lis)

# print(big_list)
while len(big_list) > 0:
    f_list = list(itertools.chain(*big_list))
    miner = min(f_list)
    maxer = max(f_list)

    counter = []
    for i in range(miner, maxer + 1):
        if i in ans_list:
            continue  # Important, to not check over it again
        count = 0
        for j in range(len(big_list)):
            if big_list[j][0] <= i <= big_list[j][1]:
                count += 1
        counter.append([i, count])

    check = sorted(counter, key=lambda x: x[1], reverse=True)
    # print("bl: ",big_list)
    # print(check)
    for i in range(25):  # REASSURING, CAN BE OPTIMISED
        for ele in big_list:
            if ele[1] >= check[0][0] and ele[0] <= check[0][0]:
                big_list.remove(ele)

    ans_list.append(check[0][0])
    # print("al",ans_list)

print(len(ans_list))
for element in ans_list:
    print(element, end=" ", sep="")
"""

n = int(input())

big_list = []
ans_list = []

for i in range(n):
    lis = list(map(int, input().split()))
    big_list.append(lis)

lis_right_min = sorted(big_list, key=lambda x: x[1])
# print(lis_right_min)

# print(big_list)
while len(lis_right_min) > 0:
    min_right = lis_right_min[0][1]

    for j in range(len(lis_right_min)):
        for ele in lis_right_min:
            if ele[0] <= min_right <= ele[1]:
                lis_right_min.remove(ele)

    ans_list.append(min_right)

print(len(ans_list))
for element in ans_list:
    print(element, end=" ", sep="")

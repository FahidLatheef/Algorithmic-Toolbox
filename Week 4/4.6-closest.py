class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str([self.x, self.y])


def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def construct_points(x, y):
    points = []
    for i in range(len(x)):
        points.append(Point(x[i], y[i]))
    return points


def minimum_distance(x, y):
    points = construct_points(x, y)
    sorted_p_x = sorted(points, key=lambda p: p.x)

    return large_size_min_distance(sorted_p_x)


def small_size_min_distance(points):
    result = 10e50
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            result = min(result, distance(points[i], points[j]))
    return result


def large_size_min_distance(p_x):
    size = len(p_x)
    half_size = int(len(p_x) / 2)

    if size <= 3:
        return small_size_min_distance(p_x)

    left_p_x = p_x[0:half_size]
    right_p_x = p_x[half_size:size]

    left_min = large_size_min_distance(left_p_x)
    right_min = large_size_min_distance(right_p_x)
    separated_min = min(left_min, right_min)

    line_l = (left_p_x[-1].x + right_p_x[0].x) / 2
    hybrid_min = compute_hybrid_min(left_p_x, right_p_x, line_l, separated_min)

    return min(separated_min, hybrid_min)


def compute_hybrid_min(left_x, right_x, line_l, wide):
    left = []
    for i in range(len(left_x)):
        if abs(left_x[i].x - line_l) <= wide:
            left.append(left_x[i])
    right = []
    for i in range(len(right_x)):
        if abs(right_x[i].x - line_l) <= wide:
            right.append(right_x[i])
    total = left + right

    total = sorted(total, key=lambda p: p.y)

    result = wide
    for i in range(len(total)):
        for j in range(i + 1, min(i + 8, len(total))):
            if abs(total[i].y - total[j].y) <= wide:
                result = min(result, distance(total[i], total[j]))

    return result


n = int(input())
left_cord = []
right_cord = []
for i in range(n):
    x, y = map(int, input().split())
    left_cord.append(x)
    right_cord.append(y)
print("{0:.6f}".format(minimum_distance(left_cord, right_cord)))

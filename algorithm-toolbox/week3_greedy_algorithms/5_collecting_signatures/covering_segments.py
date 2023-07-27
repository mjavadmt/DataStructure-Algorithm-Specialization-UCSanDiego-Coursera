# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def subscribe(a, b):
    if a[1] < b[0] or b[1] < a[0]:
        return False
    else:
        return [max(a[0], b[0]), min(a[1], b[1])]


# print(subscribe([7.5,8] , [2,7]))

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=lambda x: x[0])
    subscribe_segment = segments[0]
    for i in range(len(segments) - 1):
        if subscribe(subscribe_segment, segments[i + 1]):
            subscribe_segment = subscribe(subscribe_segment, segments[i + 1])
        else:
            points.append(subscribe_segment[0])
            subscribe_segment = segments[i + 1]
    points.append(subscribe_segment[0])
    # write your code here

    return points


# print(optimal_points([[4, 7], [1, 5], [2, 3], [3, 4]]))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

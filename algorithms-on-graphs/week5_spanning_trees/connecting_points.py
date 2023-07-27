# Uses python3
import sys
import math
from queue import PriorityQueue


def find(u, parents):
    while parents[u] != u:
        u = parents[u]
    return parents[u]


def union(x, y, ranks, parents):
    x = find(x, parents)
    y = find(y, parents)
    if x == y:
        return
    if ranks[x] > ranks[y]:
        parents[y] = x
    else:
        parents[x] = y
        if ranks[x] == ranks[y]:
            ranks[y] += 1


def distance(point_1, point_2):
    return ((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)**0.5


def clustering(x, y, k):
    nodes = []
    parents = []
    ranks = []
    priority_queue = PriorityQueue()
    for i in range(len(x)):
        nodes.append((x[i], y[i]))
        parents.append(i)
        ranks.append(1)
        for j in range(i + 1, len(x)):
            priority_queue.put((distance((x[i], y[i]), (x[j], y[j])), (i, j)))
    s = 0
    while not priority_queue.empty():
        extract_min = priority_queue.get()
        if find(extract_min[1][0], parents) != find(extract_min[1][1], parents):
            union(extract_min[1][0], extract_min[1][1], ranks, parents)
            s += extract_min[0]
    return s


def minimum_distance(x, y):
    nodes = []
    parents = []
    ranks = []
    priority_queue = PriorityQueue()
    for i in range(len(x)):
        nodes.append((x[i], y[i]))
        parents.append(i)
        ranks.append(1)
        for j in range(i + 1, len(x)):
            priority_queue.put((distance((x[i], y[i]), (x[j], y[j])), (i, j)))
    s = 0
    while not priority_queue.empty():
        extract_min = priority_queue.get()
        if find(extract_min[1][0], parents) != find(extract_min[1][1], parents):
            union(extract_min[1][0], extract_min[1][1], ranks, parents)
            s += extract_min[0]
    return s


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))

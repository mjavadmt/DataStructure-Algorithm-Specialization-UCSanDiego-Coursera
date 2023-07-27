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
    s = len(x)
    while s != k - 1:
        extract_min = priority_queue.get()
        if find(extract_min[1][0], parents) != find(extract_min[1][1], parents):
            union(extract_min[1][0], extract_min[1][1], ranks, parents)
            if s == k:
                return extract_min[0]
            s -= 1
    min_dist = float("inf")
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if find(i , parents) != find(j , parents):
                if min_dist > distance(nodes[i], nodes[j]):
                    min_dist = distance(nodes[i], nodes[j])
    return min_dist


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))

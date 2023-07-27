# # Uses python3

import sys


def relax_edges(k, w, dist, j):
    if dist[k] > dist[j] + w:
        dist[k] = dist[j] + w
        return True
    return False


def negative_cycle(adj, cost):
    V = len(adj)
    dist = [5000000 for i in range(V)]
    dist[0] = 0
    for i in range(V):
        for j in range(V):
            for k, w in zip(adj[j], cost[j]):
                changed = relax_edges(k, w, dist , j)
                if i == V - 1 and changed:
                    return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    adj_without_direction = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))



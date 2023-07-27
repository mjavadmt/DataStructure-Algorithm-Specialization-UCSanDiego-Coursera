# Uses python3

import sys
import queue


def neg_cycle(x, shortest, adj):
    shortest[x] = 0
    for i in adj[x]:
        if shortest[i] == 1:
            neg_cycle(i, shortest, adj)


def relax_edges(k, w, dist, j):
    if dist[k] > dist[j] + w:
        dist[k] = dist[j] + w
        return True
    return False


def explore(adj, s, visited):
    visited[s] = True
    for i in adj[s]:
        if not visited[i]:
            explore(adj, i, visited)


def new_explore(adj, s, visited, shortest):
    visited[s] = True
    shortest[s] = 0
    for i in adj[s]:
        if not visited[i]:
            new_explore(adj, i, visited, shortest)




def negative_cycle(adj, cost, s, distance, reachable, shortest):
    V = len(adj)
    distance[s] = 0
    find_reachable(adj, s, reachable)
    # fek konm fln khode s reachable nis 
    for i in range(V):
        for j in range(V):
            for k, w in zip(adj[j], cost[j]):
                if reachable[k]:
                    changed = relax_edges(k, w, distance, j)
                    if i == V - 1 and changed:
                        shortest[k] = 0


def find_reachable(adj, s, reachable):
    reachable[s] = 1
    for i in adj[s]:
        if not reachable[i]:
            find_reachable(adj, i, reachable)

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    V = len(adj)
    distance[s] = 0
    find_reachable(adj, s, reachable)
    for i in range(V):
        for j in range(V):
            if reachable[j]:
                for neighbor, weight in zip(adj[j], cost[j]):
                    changed = relax_edges(neighbor, weight, distance, j)
                    if changed:
                        if i == V - 1:
                            shortest[neighbor] = 0
    for i in range(n):
        if shortest[i] == 0:
            for x in adj[i]:
                if shortest[x] == 1:
                    neg_cycle(x, shortest, adj)


if __name__ == '__main__':
    input = open("read.txt","r").read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [False] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if not reachable[x]:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

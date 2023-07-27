#Uses python3

import sys
from queue import Queue

def distance(adj, s, t):
    visited = [False for i in range(len(adj))]
    distances_to_start = [-1 for i in range(len(adj))]
    distances_to_start[s] = 0
    q = Queue()
    q.put(s)
    seen_t = False
    while not q.empty():
        dequeued = q.get()
        for i in adj[dequeued]:
            if distances_to_start[i] == -1:
                q.put(i)
                distances_to_start[i] = distances_to_start[dequeued] + 1
                if i == t:
                    seen_t = True
                    break
        if seen_t:
            break
    return distances_to_start[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))

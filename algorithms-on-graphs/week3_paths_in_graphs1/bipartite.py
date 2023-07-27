# # Uses python3

import sys
from queue import Queue




def distance(adj, s ,colored_vertixes):
    
    q = Queue()
    q.put(s)
    colored_vertixes[s] = 'b'
    while not q.empty():
        dequeued = q.get()
        for i in adj[dequeued]:
            if colored_vertixes[i] == "w":
                colored_vertixes[i] = "g" if colored_vertixes[dequeued] == "b" else "b"
                q.put(i)
            else:
                if colored_vertixes[i] == colored_vertixes[dequeued]:
                    return False
    return True


def bipartite(adj):
    colored_vertixes = ['w' for i in range(len(adj))]
    for i in range(len(adj)):
        if colored_vertixes[i] == 'w' :
            if not distance(adj , i , colored_vertixes):
                return 0
    return 1


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
    print(bipartite(adj))

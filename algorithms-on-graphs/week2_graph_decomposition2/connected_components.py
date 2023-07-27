#Uses python3

import sys

def explore(vertex, adj_list , visited):
    for i in adj_list[vertex]:
        if not visited[i]:
            visited[i] = True
            explore(i , adj_list , visited)

def number_of_components(adj):
    visited = [False for i in range(len(adj))]
    cc = 0
    for i in range(len(adj)):
        if not visited[i]:
            explore(i , adj , visited)
            cc += 1
    return cc
    

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
    print(number_of_components(adj))

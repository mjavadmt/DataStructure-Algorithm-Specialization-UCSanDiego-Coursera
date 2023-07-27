#Uses python3

import sys

def explore(vertex, adj_list , visited):
    visited[vertex] = True
    for i in adj_list[vertex]:
        if not visited[i]:
            explore(i , adj_list , visited)      
    order_visiting.append(vertex)
def dfs(adj, used, x):
    #write your code here
    pass


def toposort(adj):
    used = [0] * len(adj)
    order = []
    visited = [False for i in range(vertices_count)]
    for i in range(len(adj)):
        if not visited[i] :
            explore(i , adj , visited)
    order_visiting.reverse()
    return order_visiting


if __name__ == '__main__':
    vertices_count , edges_count = map(int ,input().split()) 
    adj_list = [[] for i in range(vertices_count)]
    for j in range(edges_count):
        x , y = map(int ,input().split())
        adj_list[x-1].append(y - 1)
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    order_visiting = []
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # adj = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    order = toposort(adj_list)
    for x in order:
        print(x + 1, end=' ')


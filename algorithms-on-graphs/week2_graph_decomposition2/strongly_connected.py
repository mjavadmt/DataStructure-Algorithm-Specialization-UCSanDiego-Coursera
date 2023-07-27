#Uses python3

import sys

sys.setrecursionlimit(200000)

maximum = 0 

def explore(vertex, adj_list , visited):
    global current
    visited[vertex] = True
    current += 1
    pre[vertex] = current
    
    for i in adj_list[vertex]:
        if not visited[i]:
            explore(i , adj_list , visited)
    current += 1
    post[vertex] = current

def explore_ok(vertex, adj_list , visited):
    visited[vertex] = True
    post[vertex] = 0
    for i in adj_list[vertex]:
        if not visited[i]:
            explore_ok(i , adj_list , visited)      

def toposort(adj , reverse_adj):
    global maximum
    visited = [False for i in range(vertices_count)]
    for i in range(len(adj)):
        if not visited[i] :
            explore(i , reverse_adj , visited)
    visited = [False for i in range(vertices_count)]
    maximum = current
    get_vertex = post.index(maximum)
    scc = 0
    while False in visited:
        if not visited[get_vertex]:
            explore_ok(get_vertex , adj , visited)
            scc += 1
        maximum = max(post)
        get_vertex = post.index(maximum)
    return scc


def number_of_strongly_connected_components(adj, reverse_adj):
    result = 0
    global maximum
    visited = [False for i in range(vertices_count)]
    for i in range(len(adj)):
        if not visited[i] :
            explore(i , reverse_adj , visited)
    visited = [False for i in range(vertices_count)]
    maximum = current
    get_vertex = post.index(maximum)
    scc = 0
    while False in visited:
        if not visited[get_vertex]:
            explore_ok(get_vertex , adj , visited)
            scc += 1
        maximum = max(post)
        get_vertex = post.index(maximum)
    return scc
    #write your code here

if __name__ == '__main__':
    vertices_count , edges_count = map(int ,input().split()) 
    adj_list = [[] for i in range(vertices_count)]
    reverse_adj = [[] for _ in range(vertices_count)]
    for j in range(edges_count):
        x , y = map(int ,input().split())
        adj_list[x-1].append(y - 1)
        reverse_adj[y - 1].append(x - 1)
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # adj = [[] for _ in range(n)]
    
    pre = [0 for i in range(vertices_count)]
    post = [0 for i in range(vertices_count)]
    current = 0
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    #     reverse_adj[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj_list, reverse_adj))

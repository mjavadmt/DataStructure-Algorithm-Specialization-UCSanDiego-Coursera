#Uses python3

import sys

def explore(vertex, adj_list , visited, wanted):
    visited[vertex] = True
    if vertex == wanted:
        return 1
    for i in adj_list[vertex]:
        if not visited[i]:
            if explore(i , adj_list , visited , wanted) == 1:
                return 1
    return 0
def reach(adj, x, y , vertixes_count):
    visited = [False for i in range(vertices_count)]
    return explore(x , adj , visited , y)

if __name__ == '__main__':
    vertices_count , edges_count = map(int ,input().split()) 
    adj_list = [[] for i in range(vertices_count)]
    for j in range(edges_count):
        x , y = map(int ,input().split())
        adj_list[x-1].append(y - 1)
        adj_list[y-1].append(x - 1)
    u , v = map(int ,input().split())
    print(reach(adj_list , u - 1, v - 1 , vertices_count))
    
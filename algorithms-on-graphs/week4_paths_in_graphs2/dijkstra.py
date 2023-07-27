# Uses python3

import sys
from queue import PriorityQueue

class MinHeap:
    def __init__(self):
        """
        On this implementation the heap list is initialized with a value
        """
        self.heap_list = [0]
        self.current_size = 0

    def sift_up(self, i):
        """
        Moves the value up in the tree to maintain the heap property.
        """
        # While the element is not the root or the left element
        while i // 2 > 0:
            # If the element is less than its parent swap the elements
            if self.heap_list[i][0] < self.heap_list[i // 2][0]:
                self.heap_list[i], self.heap_list[i //
                                                  2] = self.heap_list[i // 2], self.heap_list[i]
            # Move the index to the parent to keep the properties
            i = i // 2

    def insert(self, k):
        """
        Inserts a value into the heap
        """
        # Append the element to the heap
        self.heap_list.append(k)
        # Increase the size of the heap.
        self.current_size += 1
        # Move the element to its position from bottom to the top
        self.sift_up(self.current_size)

    def sift_down(self, i):
        # if the current node has at least one child
        while (i * 2) <= self.current_size:
            # Get the index of the min child of the current node
            mc = self.min_child(i)
            # Swap the values of the current element is greater than its min child
            if self.heap_list[i][0] > self.heap_list[mc][0]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        # If the current node has only one child, return the index of the unique child
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
            # Herein the current node has two children
            # Return the index of the min child according to their values
            if self.heap_list[i*2][0] < self.heap_list[(i*2)+1][0]:
                return i * 2
            else:
                return (i * 2) + 1

    def index(self, value):
        for i in range(len(self.heap_list)):
            if self.heap_list[i] == value:
                return i
        return -1

    def change_priority(self, idx, new_value):
        self.heap_list[idx] = new_value
        self.sift_up(idx)

    def delete_min(self):
        # Equal to 1 since the heap list was initialized with a value
        if len(self.heap_list) == 1:
            return 'Empty heap'

        # Get root of the heap (The min value of the heap)
        root = self.heap_list[1]

        # Move the last value of the heap to the root
        self.heap_list[1] = self.heap_list[self.current_size]

        # Pop the last value since a copy was set on the root
        *self.heap_list, _ = self.heap_list

        # Decrease the size of the heap
        self.current_size -= 1

        # Move down the root (value at index 1) to keep the heap property
        self.sift_down(1)

        # Return the min value of the heap
        return root

    def __repr__(self):
        return f"{self.heap_list}"


def distance(adj, cost, s, t):
    dist = [float('inf') for i in range(len(adj))]
    prev = [None for i in range(len(adj))]
    priority_min_queue = MinHeap()
    dist[s] = 0
    for i in range(len(dist)):
        # heapq.heappush(min_heap , (dist[i] , i))
        priority_min_queue.insert((dist[i] , i))
    
    while len(priority_min_queue.heap_list) != 1:
        extraxt_min = priority_min_queue.delete_min()
        for neighbor , weight in zip(adj[extraxt_min[1]] , cost[extraxt_min[1]]):
            if dist[neighbor] > dist[extraxt_min[1]] + weight:
                idx = priority_min_queue.index((dist[neighbor],neighbor))
                assert idx >= 0
                dist[neighbor] = dist[extraxt_min[1]] + weight
                prev[neighbor] = extraxt_min[1]
                priority_min_queue.change_priority(idx , (dist[neighbor], neighbor))
    if dist[t] == float('inf'):
        return -1
    return dist[t]


# distance([1, 2, 3], 3, 1, 1)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))

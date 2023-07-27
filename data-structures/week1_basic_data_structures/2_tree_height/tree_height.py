# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def recursive_height(dictionary_instances, ind):
    if len(dictionary_instances[ind]) == 0:
        return 1
    # if len(dictionary_instances[ind] == 1):
    #     return recursive_height(dictionary_instances, dictionary_instances[ind][0]) + 1
    # if len(dictionary_instances[ind]) == 2:
    #     return max(recursive_height(dictionary_instances,dictionary_instances[ind][0]),
    #                recursive_height(dictionary_instances,dictionary_instances[ind][1])) + 1
    max_so_far = 0
    for i in dictionary_instances[ind]:
        compute_sub_tree = recursive_height(dictionary_instances, i) + 1
        if compute_sub_tree > max_so_far:
            max_so_far = compute_sub_tree
    return max_so_far


def main():
    n = int(input())
    # n = 100
    parents = list(map(int, input().split()))
    # parents = list(map(int, "32 7 51 65 35 72 63 84 60 87 33 24 43 86 9 68 26 64 6 43 32 35 18 82 33 75 94 19 59 12 54 29 75 -1 12 12 58 7 17 60 75 95 64 95 51 76 50 87 53 65 10 33 46 93 64 82 5 80 10 12 12 50 87 59 68 50 42 95 10 9 43 64 33 36 20 95 75 42 75 15 59 50 4 41 43 18 43 83 72 81 1 43 1 60 43 68 93 63 95 63".split()))
    make_dict = {}
    for i in range(n):
        make_dict[i] = []
    ind = 0
    for i in range(n):
        if parents[i] != -1:
            make_dict[parents[i]].append(i)
        else:
            ind = i
    print(recursive_height(make_dict, ind))
    # print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()

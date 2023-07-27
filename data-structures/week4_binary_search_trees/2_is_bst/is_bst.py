import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class Node:
    def __init__(self, a, b, c):
        self.key = a
        self.left = b
        self.right = c
    def __str__(self):
        return "slm"
    def __repr__(self):
        return f"key:{self.key} left:{self.left} right:{self.right}"



def IsBinarySearchTree(tree):
    stack = [(float('-inf'), tree[0], float('inf'))]
    while stack:
        min_so_far, root, max_so_far = stack.pop()
        if root.key < min_so_far or root.key >= max_so_far:
            return False
        if root.left != -1:
            stack.append((min_so_far, tree[root.left], root.key))
        if root.right != -1:
            stack.append((root.key, tree[root.right], max_so_far))
    return True


def main():
    n_nodes = int(input())
    nodes = []
    for i in range(n_nodes):
        a, b, c = map(int, input().split())
        node = Node(a, b, c)
        nodes.append(node)
    if n_nodes == 0 or IsBinarySearchTree(nodes):
        print('CORRECT')
    else:
        print('INCORRECT')


threading.Thread(target=main).start()
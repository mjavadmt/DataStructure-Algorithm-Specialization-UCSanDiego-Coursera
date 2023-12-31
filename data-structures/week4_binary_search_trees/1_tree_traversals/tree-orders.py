# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        # self.n = int(inpu/t())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self, root):
        if root == -1:
            return
        self.inOrder(self.left[root])
        print(self.key[root] , end=" ")
        self.inOrder(self.right[root])
        # Finish the implementation
        # You may need to add a new recursive method to do that


    def preOrder(self, root):
        if root == -1:
            return
        print(self.key[root],end=" ")
        self.preOrder(self.left[root])
        self.preOrder(self.right[root])
        # Finish the implementation
        # You may need to add a new recursive method to do that


    def postOrder(self , root):
        if root == -1:
            return
        self.postOrder(self.left[root])
        self.postOrder(self.right[root])
        print(self.key[root],end=" ")
        # Finish the implementation
        # You may need to add a new recursive method to do that



def main():
    tree = TreeOrders()
    tree.read()
    tree.inOrder(0)
    print()
    tree.preOrder(0)
    print()
    tree.postOrder(0)
    print()
    # print(" ".join(str(x) for x in tree.inOrder(0)))
    # print(" ".join(str(x) for x in tree.preOrder(0)))
    # print(" ".join(str(x) for x in tree.postOrder(0)))


threading.Thread(target=main).start()

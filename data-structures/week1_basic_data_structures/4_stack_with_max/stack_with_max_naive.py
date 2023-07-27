# python3
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max_list = []

    def Push(self, a):
        self.__stack.append(a)
        if not self.max_list:
            self.max_list.append(a)
        else:
            if self.max_list[-1] <= a:
                self.max_list.append(a)
    def Pop(self):
        assert (len(self.__stack))
        popped_element = self.__stack.pop()
        if popped_element == self.max_list[-1]:
            self.max_list.pop()

    def Max(self):
        assert (len(self.__stack))
        return self.max_list[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    # num_queries = 10
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        # query = input().split()
        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert (0)

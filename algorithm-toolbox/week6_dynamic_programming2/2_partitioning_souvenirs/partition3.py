    # Uses python3
import sys
import itertools
import numpy


def partition3(A):
    total_weight = sum(A)
    if len(A) < 3:
        return 0
    elif total_weight % 3 != 0:
        return 0
    return partitions(total_weight // 3, len(A), A)


def partitions(W, n, items):
    count = 0
    value = numpy.zeros((W + 1, n + 1))
    for i in range(1, W + 1):
        for j in range(1, n + 1):
            value[i][j] = value[i][j - 1]
            if items[j - 1] <= i:
                temp = value[i - items[j - 1]][j - 1] + items[j - 1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W:
                count += 1

    if count < 3:
        return 0
    else:
        return 1


# it computes the best way for w from 0 ta W that what is the best sum of them
# until the ith item


if __name__ == '__main__':
    # partition3([1,2,3,4,6,11])
    partition3([1,2,3,4,6,8])
    # partition3([1,1,4])
    # input = sys.stdin.read()
    # n, *A = list(map(int, input.split()))
    # print(partition3(A))

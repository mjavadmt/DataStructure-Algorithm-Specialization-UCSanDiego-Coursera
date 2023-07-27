# Uses python3
import sys
import re
import numpy


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def min_max(i, j, max_l, min_l, operations):
    min_so_far = sys.maxsize
    max_so_far = - min_so_far
    # 1 , 4 = 0 , 3
    # 0 , 1 | 2 , 3
    for k in range(i, j):
        m1 = evalt(max_l[i][k], max_l[k + 1][j], operations[k])
        m2 = evalt(max_l[i][k], min_l[k + 1][j], operations[k])
        m3 = evalt(min_l[i][k], min_l[k + 1][j], operations[k])
        m4 = evalt(min_l[i][k], max_l[k + 1][j], operations[k])
        min_so_far = min(min_so_far, m1, m2, m3, m4)
        max_so_far = max(max_so_far, m1, m2, m3, m4)    
    return min_so_far, max_so_far


def get_maximum_value(dataset):
    # write your code here
    splitting = re.split(r'(\D)', dataset)
    list_numbers = []
    list_operations = []
    for i in splitting:
        if i != "+" and i != "-" and i != '*':
            list_numbers.append(int(i))
        else:
            list_operations.append(i)
    two_dimensional_maximum = numpy.zeros((len(list_numbers), len(list_numbers)))
    two_dimensional_minimum = numpy.zeros((len(list_numbers), len(list_numbers)))

    for i in range(len(list_numbers)):
        two_dimensional_minimum[i][i], two_dimensional_maximum[i][i] = list_numbers[i], list_numbers[i]
    for s in range(1, len(list_numbers)):
        for i in range(len(list_numbers) - s):
            j = i + s
            two_dimensional_minimum[i][j], two_dimensional_maximum[i][j] = min_max(i, j, two_dimensional_maximum,
                                                                                   two_dimensional_minimum,
                                                                                   list_operations)

    return int(two_dimensional_maximum[0][-1])


if __name__ == "__main__":
    print(get_maximum_value(input()))

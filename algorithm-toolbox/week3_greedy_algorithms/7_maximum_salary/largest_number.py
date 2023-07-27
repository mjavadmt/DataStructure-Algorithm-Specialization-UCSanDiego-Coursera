# Uses python3

import sys


def make_sort(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            a = int(l[i] + l[j])
            b = int(l[j] + l[i])
            if b > a:
                l[i], l[j] = l[j], l[i]


def largest_number(a):
    # write your code here
    make_sort(a)
    res = ""
    for x in a:
        res += x
    return res


# print(largest_number(['34', '3', '321']))
# print(largest_number(['9', '4', '6', '1', '9']))
# print(largest_number(['2','21']))
# print(largest_number(['23','39', '92']))
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

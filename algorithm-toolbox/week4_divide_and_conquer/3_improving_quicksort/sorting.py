# Uses python3
import sys
import random




def randomized_quick_sort(a, l, r):
    sorted_list = split_randomized_sort(a)
    for i in range(len(sorted_list)):
        a[i] = sorted_list[i]


def split_randomized_sort(l):
    if len(l) == 1 or len(l) == 0:
        return l
    rnd = random.randint(0, len(l) - 1)
    l[0], l[rnd] = l[rnd], l[0]
    middle = [l[0]]
    left = []
    right = []
    for i in range(1, len(l)):
        if l[0] < l[i]:
            right.append(l[i])
        elif l[0] > l[i]:
            left.append(l[i])
        else:
            middle.append(l[i])
    a = split_randomized_sort(left)
    b = split_randomized_sort(right)

    return a + middle + b


# my_list = [2, 2, 6, 3,2, 5, 7,2, 8,  4]
# randomized_quick_sort(my_list, 0, len(my_list) - 1)
# print(my_list)

# ssuu = [7, 2, 8, 4, 4, 4, 4, 5, 7, 2, 2, 4, 7, 8, 9, 2, 4, 5, 6, 3, -23, -21, 65, 32]
# randomized_quick_sort(ssuu, 0, 5)
# print(ssuu)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

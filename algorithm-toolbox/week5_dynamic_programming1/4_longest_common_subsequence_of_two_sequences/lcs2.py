# Uses python3

import sys

# longest common subsequence of two sequences is sub problem of edit distance ignoring mismatches
# and then coming back from bottom right corner of the 2d list and reach to left top corner of 2d list
# such that in each iteration we'll consider which of the insertion, deletion or matches we used .


def edit_distance(x, y):
    l = []
    for i in range(len(y) + 1):
        m = []
        for j in range(len(x) + 1):
            m.append(0)
        l.append(m)
    for i in range(len(y) + 1):
        for j in range(len(x) + 1):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                l[i][j] = l[i][j - 1] + 1
            elif j == 0:
                l[i][j] = l[i - 1][j] + 1
            elif x[j - 1] == y[i - 1]:
                l[i][j] = min(l[i - 1][j - 1], l[i][j - 1] + 1, l[i - 1][j] + 1)
            elif x[j - 1] != y[i - 1]:
                l[i][j] = min(l[i][j - 1] + 1, l[i - 1][j] + 1)
    matches_number = 0
    string = ""
    while i != 0 and j != 0:
        if x[j - 1] == y[i - 1] and l[i - 1][j - 1] <= l[i][j - 1] and l[i - 1][j - 1] <= l[i - 1][j]:
            matches_number += 1
            string += str(y[i - 1])
            i -= 1
            j -= 1
        else:
            if l[i][j - 1] < l[i - 1][j]:
                j -= 1
            else:
                i -= 1
    print(string)
    return matches_number


print(edit_distance([19,0,17,13,6], [16,19,0,13,10,18,1,3]))


def my_fraction(up, down):
    start = 1
    make_fraction = 0
    while make_fraction != up/down:
        if make_fraction + 1/start <= up/down:
            make_fraction += 1/start
        else:
            start += 1
    c = 2
my_fraction(6, 14)




def lcs2(a, b):
    # write your code here
    return edit_distance(a,b)


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#
#     n = data[0]
#     data = data[1:]
#     a = data[:n]
#
#     data = data[n:]
#     m = data[0]
#     data = data[1:]
#     b = data[:m]
#
#     print(lcs2(a, b))

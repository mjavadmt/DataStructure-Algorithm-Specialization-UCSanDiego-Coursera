# Uses python3

import sys


def edit_distance(a, b, c):
    d_third_D = []
    for i in range(len(a) + 1):
        d_second_D = []
        for j in range(len(b) + 1):
            d_first_D = []
            for k in range(len(c) + 1):
                d_first_D.append(0)
            d_second_D.append(d_first_D)
        d_third_D.append(d_second_D)

    for x in range(1, len(a) + 1):
        for y in range(1, len(b) + 1):
            for z in range(1, len(c) + 1):
                node_match = d_third_D[x - 1][y - 1][z - 1] + 1
                node_mismatch = d_third_D[x - 1][y - 1][z - 1]
                node3 = d_third_D[x - 1][y][z]
                node5 = d_third_D[x][y - 1][z]
                node6 = d_third_D[x][y][z - 1]
                if a[x - 1] == b[y - 1] == c[z - 1]:
                    d_third_D[x][y][z] = max(node3,  node5, node6, node_match)
                else:
                    d_third_D[x][y][z] = max( node3, node5, node6, node_mismatch)
    return d_third_D[-1][-1][-1]


# edit_distance([1, 2, 3], [2, 1, 3], [1, 3, 5])
# edit_distance([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7])


def lcs3(a, b, c):
    return edit_distance(a,b,c)

# print(lcs3("abcd", "adcb", [1, 3, 5]))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))

# Uses python3
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
                l[i][j] = min(l[i - 1][j - 1] + 1, l[i][j - 1] + 1, l[i - 1][j] + 1)
    return l[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))

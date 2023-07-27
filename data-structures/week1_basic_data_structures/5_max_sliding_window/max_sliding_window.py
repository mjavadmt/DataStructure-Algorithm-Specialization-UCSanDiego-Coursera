# python3


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


def max_slice(sequence, m):
    l_indexes = []
    l_maxes = []
    for i in range(len(sequence) - m):
        if not (i <= l_indexes[0] <= i + m - 1):
            l_indexes.remove(l_indexes[0])
        if not l_indexes:
            l_indexes.append(i)
        else:
            print()
        # if i >= 3:
        #     l_maxes.append(sequence[l_indexes[0]])

    return 0


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

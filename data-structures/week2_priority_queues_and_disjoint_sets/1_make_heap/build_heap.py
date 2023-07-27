# python3

def sift_down(ind, heap_list, swaps_list):
    children_1, children_2 = 2 * ind + 1, 2 * ind + 2
    swaps_count = 0
    while children_2 < len(heap_list) and heap_list[ind] > min(heap_list[children_1], heap_list[children_2]):
        if min(heap_list[children_1], heap_list[children_2]) == heap_list[children_1]:
            heap_list[children_1], heap_list[ind] = heap_list[ind], heap_list[children_1]
            swaps_list.append((ind, children_1))
            ind = children_1
        else:
            heap_list[children_2], heap_list[ind] = heap_list[ind], heap_list[children_2]
            swaps_list.append((ind, children_2))
            ind = children_2
        swaps_count += 1
        children_1, children_2 = 2 * ind + 1, 2 * ind + 2
    if children_1 < len(heap_list) and heap_list[children_1] < heap_list[ind]:
        heap_list[children_1], heap_list[ind] = heap_list[ind], heap_list[children_1]
        swaps_list.append((ind, children_1))
        swaps_count += 1
    return swaps_count


# heap_l = [5, 4, 3, 2, 1]
#
# second = [4, 3, 8, 2, 6, 7]


# sift_down(0, heap_l)


def build_heap(data):
    swaps_list = []
    swaps_count = 0
    for i in range(int((len(data) - 1) / 2), -1, -1):
        swaps_count += sift_down(i, data, swaps_list)
    return swaps_list


# build_heap(second)


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

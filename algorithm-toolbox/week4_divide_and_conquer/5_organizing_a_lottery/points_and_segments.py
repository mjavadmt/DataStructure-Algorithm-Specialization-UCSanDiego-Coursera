# Uses python3
import sys


def binary_search_for_right(a, x, left, right):
    if left > right:
        return left
    mid = int((left + right) / 2)
    if a[mid] > x:
        return binary_search_for_right(a, x, left, mid - 1)
    elif a[mid] < x:
        return binary_search_for_right(a, x, mid + 1, right)
    else:
        ind = mid
        for i in range(mid - 1, -1, -1):
            if a[i] != a[mid]:
                break
            ind -= 1
        return ind


# first = binary_search_for_right([2, 5, 7, 10, 10, 10, 13, 15, 16], 13, 0, 8)
# print(first)


def binary_search_for_left(a, x, left, right):
    if left > right:
        return right
    mid = int((left + right) / 2)
    if a[mid] > x:
        return binary_search_for_left(a, x, left, mid - 1)
    elif a[mid] < x:
        return binary_search_for_left(a, x, mid + 1, right)
    else:
        ind = mid
        for i in range(mid + 1, len(a)):
            if a[i] != a[mid]:
                break
            ind += 1
        return ind


# first = binary_search_for_left([1, 1, 1, 1], 2, 0, 3)
# print(first)


def fast_count_segments(starts, ends, points):
    length = len(starts)
    cnt = []
    starts.sort()
    ends.sort()
    for p in points:
        l = binary_search_for_left(starts, p, 0, length - 1)
        r = binary_search_for_right(ends, p, 0, length - 1)
        cnt.append(l + 1 - r)  # (l+1)+(length-r)-length
    # write your code here
    return cnt


# starts_points = [-10]
# ends_points = [10]
# points = [-100, 100, 0]
# print(fast_count_segments(starts_points, ends_points, points))


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

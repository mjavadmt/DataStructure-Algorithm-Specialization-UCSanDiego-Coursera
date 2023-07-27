# python3
import sys


def find_the_nearest_element(ind, position, l):
    if len(l) == 0:
        return -1 , -1
    for i in range(ind + 1, len(l)):
        if position < l[i]:
            return i - 1, l[i - 1]
    return len(l) - 1, l[-1]


# print(find_the_nearest_element(1, 775, [200, 375, 550, 750]))


def compute_min_refills(distance, tank, stops):
    # write your code here
    before_start = -1
    start = 0
    current_index = 0
    stops_count = 0
    while start < distance:
        before_start = start
        start += tank
        if start >= distance:
            break
        current_index, start = find_the_nearest_element(current_index, start, stops)
        stops_count += 1
        if before_start == start:
            return -1
    return stops_count

print(compute_min_refills(100 , 50 , [40 , 100]))
# print(compute_min_refills(10, 3, [1, 2, 5, 9]))
# print(compute_min_refills(950, 400, [200, 375, 550, 750]))
# print(compute_min_refills(200,250,[100,150]))
if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

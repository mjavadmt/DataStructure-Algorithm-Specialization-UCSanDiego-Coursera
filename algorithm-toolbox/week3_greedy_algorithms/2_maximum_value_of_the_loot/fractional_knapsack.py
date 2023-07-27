# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    picked_weight = 0
    merge_vw = [(round(values[i]/weights[i], 9), weights[i]) for i in range(len(weights))]
    merge_vw.sort(key=lambda x: x[0], reverse=True)
    initializer = 0
    while picked_weight < capacity:
        if initializer == len((merge_vw)):
            return round(value, 9)
        if picked_weight + merge_vw[initializer][1] <= capacity:
            value += merge_vw[initializer][0] * merge_vw[initializer][1]
            picked_weight += merge_vw[initializer][1]
        else:
            value += round((capacity - picked_weight) * merge_vw[initializer][0], 9)
            picked_weight = capacity
        initializer += 1

    # print(merge_vw)
    return value


# print(get_optimal_value(50, [20, 50, 30], [60, 100, 120]))
# print(get_optimal_value(10, [30], [500]))
# print(get_optimal_value(1000 , [30] , [500]))
if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

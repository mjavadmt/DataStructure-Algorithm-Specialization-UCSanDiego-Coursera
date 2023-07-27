# Uses python3
import sys




def optimal_weight(W, w):
    # write your code here
    return knapsack_without_repetition_dp(w,W)


def knapsack_without_repetition_dp(weights_values, max_weight):
    values = []
    for i in range(len(weights_values) + 1):
        m = []
        for j in range(max_weight + 1):
            m.append(0)
        values.append(m)
    for i in range(1, len(weights_values) + 1):
        for j in range(1, max_weight + 1):
            if j < weights_values[i - 1]:
                values[i][j] = values[i - 1][j]
            else:
                values[i][j] = max(values[i - 1][j],
                                   values[i - 1][j - weights_values[i - 1]] + weights_values[i - 1])
    return values[-1][-1]


knapsack_without_repetition_dp([2 , 3 , 5 , 6 , 7], 8)

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     W, n, *w = list(map(int, input.split()))
#     print(optimal_weight(W, w))

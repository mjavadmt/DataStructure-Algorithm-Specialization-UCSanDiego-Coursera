# Uses python3
import sys



def optimal_summands(n):
    summands = []
    initializer = 1
    s = 0
    while s <= n:
        s += initializer
        summands.append(initializer)
        initializer += 1
    summands.remove(summands[-1])
    summands.remove(summands[-1])
    summands.append(n - sum(summands))
    return summands
# print(optimal_summands(1))
# print(optimal_summands(2))
# print(optimal_summands(3))
# print(optimal_summands(27))
# print(optimal_summands(29))
# print(optimal_summands(28))

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

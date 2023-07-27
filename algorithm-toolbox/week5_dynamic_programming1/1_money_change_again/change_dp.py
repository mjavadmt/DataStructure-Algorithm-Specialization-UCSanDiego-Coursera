# Uses python3
import sys

def get_change(m):
    l_numbers = [0]
    for i in range(m):
        l_numbers.append(sys.maxsize)
    l_coins = [1, 3, 4]
    for i in range(1,m+1):
        for j in l_coins:
            if j <= i:
                if l_numbers[i] > l_numbers[i-j] + 1:
                    l_numbers[i] = l_numbers[i-j] + 1
    return l_numbers[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

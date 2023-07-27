# Uses python3
import sys


def find_nearest_coin(coins, m):
    return min([i for i in coins if i <= m], key=lambda x: abs(x - m))


def get_change(m):
    remained_coin = m
    number_of_coins = 0
    while remained_coin > 0:
        remained_coin -= find_nearest_coin([1, 5, 10], remained_coin)
        number_of_coins += 1
    return number_of_coins




if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

# Uses python3
import sys


def my_gcd(a, b):
    #     gcd(a,b) = gcd(rem(a,b) , b)
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def lcm_naive(a, b):
    return int((a * b) / my_gcd(a, b))


# print(lcm_naive(11,5))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

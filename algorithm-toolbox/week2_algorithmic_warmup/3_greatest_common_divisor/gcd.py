# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def my_gcd(a, b):
    #     gcd(a,b) = gcd(rem(a,b) , b)
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def recursive_gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    return recursive_gcd(min(a, b), max(a, b) % min(a, b))



# print(recursive_gcd(18, 48))

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(my_gcd(a, b))

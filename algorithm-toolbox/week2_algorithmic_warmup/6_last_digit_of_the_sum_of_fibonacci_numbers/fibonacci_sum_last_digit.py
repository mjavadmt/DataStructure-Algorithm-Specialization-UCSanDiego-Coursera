# Uses python3
import sys


def fibo(n):
    a = 0
    b = 1
    s = 0
    for i in range(n % 60):
        s += b
        s %= 10
        a, b = b, (a + b) % 10

    return s


# print(fibo(1))


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    mysum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        mysum += current

    return mysum % 10

# print(fibonacci_sum_naive(613455))

if __name__ == '__main__':
    input1 = sys.stdin.read()
    n = int(input1)
    print(fibo(n))


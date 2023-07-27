# Uses python3
from sys import stdin

def sum_squares_fib(n):
    a = 0
    b = 1
    for i in range((n % 60)):
        a, b = b, (a + b) % 10
    return a

def multiply_two(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (sum_squares_fib(n) * sum_squares_fib(n+1)) % 10

# print(multiply_two(3))




if __name__ == '__main__':
    n = int(stdin.read())
    print(multiply_two(n))

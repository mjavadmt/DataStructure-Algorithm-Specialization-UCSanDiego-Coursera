# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if to < 2:
        return 1
    a = 1
    b = 1
    s = 0
    # from = 3 mishmare
    if from_ < 3:
        if from_ == 2 :
            s = 1
        else:
            s = 2
    if to == 2:
        return s
    if to < 2:
        if to == 1 :
            return 1
        if to == 0 :
            return 0
    for i in range(to - 2):
        a, b = b, (a + b) % 10
        if i+3 >= from_:
            s += b
    return s % 10
# not measured in good time

def fibo(n):
    a = 0
    b = 1   
    s = 0
    for i in range(n % 60):
        s += b
        s %= 10
        a, b = b, (a + b) % 10

    return s


def receive_two(m , n):
    remainder = fibo(n) - fibo(m - 1)
    if remainder < 0 :
        return remainder + 10
    return remainder

print(receive_two(10 , 10))

# if __name__ == '__main__':
#     input = sys.stdin.read();
#     from_, to = map(int, input.split())
#     print(receive_two(from_, to))
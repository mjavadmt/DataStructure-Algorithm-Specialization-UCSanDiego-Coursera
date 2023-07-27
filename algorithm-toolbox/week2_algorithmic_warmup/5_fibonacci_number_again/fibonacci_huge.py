# Uses python3
import sys


def find_period(s, to_find):
    start = len(to_find)
    try:
        while True:
            first_cmp = ""
            second_cmp = ""
            ind = s.index(to_find, start)
            for i in range(0, ind):
                first_cmp += s[i]
                second_cmp += s[i + ind]
            if first_cmp == second_cmp:
                return first_cmp
            start = ind + 1
    except:
        return False


# print(find_period())


def find_rem_huge_fib(n, m):
    whole_str = "0,1,"
    make_str = ""
    # make fibonacci
    l_fibo = [0, 1]
    l_rem_fibo = [0, 1]
    made_period = ""
    for i in range(2, n + 1):
        fibo_i = l_fibo[i - 1] + l_fibo[i - 2]
        l_fibo.append(fibo_i)
        rem = fibo_i % m
        l_rem_fibo.append(rem)
        whole_str += str(rem)
        whole_str += ','
        if str(l_rem_fibo[i - 2]) + str(l_rem_fibo[i - 1]) + str(l_rem_fibo[i]) == '011':
            period = find_period(whole_str, '0,1,1')
            if period:
                split_with_comma = period.split(',')
                return split_with_comma[n % (len(split_with_comma)-1)]
    return l_fibo[-1] % m
    # make to_find string until the fibo(n) is less than m


# print(find_rem_huge_fib(3816213588, 239))
# print(find_rem_huge_fib(2015, 3))
# print(find_rem_huge_fib(239, 1000))


# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current = 1
#     list_remainder = [0, 1]
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         list_remainder.append(current % m)
#     print(list_remainder)
#     print(list_remainder[108])
#     return current % m

# print(get_fibonacci_huge_naive(478, 239))

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(find_rem_huge_fib(n, m))

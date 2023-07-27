# Uses python3
def calc_fib(n):
    if n == 0:
        return 0
    list_fib = [0, 1]
    for i in range(n-1):
        list_fib.append(list_fib[-1] + list_fib[-2])
    return list_fib[-1]


n = int(input())
print(calc_fib(n))

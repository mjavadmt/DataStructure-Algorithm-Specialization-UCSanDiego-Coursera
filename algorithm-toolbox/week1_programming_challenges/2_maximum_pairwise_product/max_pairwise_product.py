# python3


def max_pairwise_product(numbers):
    # n = len(numbers)
    # max_product = 0
    # for first in range(n):
    #     for second in range(first + 1, n):
    #         max_product = max(max_product,
    #             numbers[first] * numbers[second])

    # return max_product
    # their implementation -----------
    # mine implementation ------------
    first_max = numbers.pop(numbers.index(max(numbers)))
    second_max = numbers.pop(numbers.index(max(numbers)))
    return first_max * second_max


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

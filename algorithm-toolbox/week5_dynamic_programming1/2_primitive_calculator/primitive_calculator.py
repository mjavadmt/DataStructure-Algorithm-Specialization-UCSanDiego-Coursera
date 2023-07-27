# Uses python3
import sys


def optimal_sequence(n):
    sequence_n = [[0], [1], [1, 2]]
    if n == 1:
        return [1]
    fill_count = [0, 0, 1]
    for i in range(3, n + 1):
        rem_three = i % 3
        rem_two = i % 2
        count_divider_three = fill_count[(i - rem_three) // 3]
        count_divider_two = fill_count[(i - rem_two) // 2]
        if rem_three + count_divider_three < rem_two + count_divider_two:
            fill_count.append(rem_three + 1 + count_divider_three)
            if rem_three == 0:
                sequence_n.append(sequence_n[(i - rem_three) // 3] + [i])
            elif rem_three == 1:
                sequence_n.append(sequence_n[(i - rem_three) // 3] + [i - rem_three, i + 1 - rem_three])
            elif rem_three == 2:
                sequence_n.append(
                    sequence_n[(i - rem_three) // 3] + [i - rem_three, i + 1 - rem_three, i + 2 - rem_three])
        else:
            fill_count.append(rem_two + 1 + count_divider_two)
            if rem_two == 0:
                sequence_n.append(sequence_n[(i - rem_two) // 2] + [i])
            else:
                sequence_n.append(sequence_n[(i - rem_two) // 2] + [i - rem_two, i + 1 - rem_two])
    return sequence_n[-1]
optimal_sequence(21)

def list_operations_optimal(n):
    if n == 0:
        return 0
    l_functions = [['+', 1], ['+', 2], ['+', 3], ['*', 1], ['*', 2], ['*', 10]]
    min_operation = sys.maxsize
    for i in l_functions:
        if n >= i[1]:
            if i[0] == '+':
                updated_min = list_operations_optimal(n - i[1]) + 1
                if min_operation > updated_min:
                    min_operation = updated_min
            if i[0] == '*':
                # this part should be updated for remainder n % i[1]
                # we should count another function just for + function i mean if
                # our example is 37 we should see (37 - 7)/10 + 1 +
                # count for 7 that just needs to iterate through the plus functions
                updated_min = list_operations_optimal(n // i[1]) + 1
                if min_operation > updated_min:
                    min_operation = updated_min
# def empty_square(a, b):
#     for i in range(1, a+1):
#         if int((a-b)/2) < i <= int((a+b)/2):
#             print('*' * int((a - b) / 2) + ' ' * b + '*' * int((a - b) / 2))
#         else:
#             print('*' * a)


# empty_square(4, 0)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

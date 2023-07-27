# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    left_m = get_majority_element(a, left, (left + right - 1)//2 + 1)
    right_m = get_majority_element(a, (left + right - 1)//2 + 1, right)
    left_count = 0
    for i in range(left, right):
        if a[i] == left_m:
            left_count += 1
    if left_count > (right-left)//2:
        return left_m

    right_count = 0
    for i in range(left, right):
        if a[i] == right_m:
            right_count += 1
    if right_count > (right-left)//2:
        return right_m

    return -1
print(get_majority_element([2,2],0,2))

def my_majority(l):
    if len(l) == 1:
        return l[0]
    a = my_majority(l[:len(l)//2])
    b = my_majority(l[len(l)//2:])
    count_a = 0
    count_b = 0
    if a != -1:
        for i in l:
            if i == a:
                count_a += 1
        if count_a > len(l)/2 :
            return a
    if b != -1: 
        for i in l:
            if i == b:
                count_b += 1
        if count_b > len(l)/2 :
            return b
    return -1
print(my_majority([2,4]))


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     if get_majority_element(a, 0, n) != -1:
#         print(1)
#     else:
#         print(0)

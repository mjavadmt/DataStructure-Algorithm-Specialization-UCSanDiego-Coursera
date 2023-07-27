# Uses python3
import sys


def Merge_list(left_list, right_list):
    sorted_list = []
    so_far_right = 0
    so_far_left = 0
    inversion_number = 0
    s = 0
    while so_far_left != len(left_list) or so_far_right != len(right_list):
        if so_far_left != len(left_list) and so_far_right != len(right_list):
            if left_list[so_far_left] > right_list[so_far_right]:
                sorted_list.append(right_list[so_far_right])
                so_far_right += 1
                s += 1
            else:
                sorted_list.append(left_list[so_far_left])
                so_far_left += 1
                inversion_number += s
        else:
            if so_far_left != len(left_list):
                sorted_list.append(left_list[so_far_left])
                so_far_left += 1
                inversion_number += s
            else:
                # dont do anything
                sorted_list.append(right_list[so_far_right])
                so_far_right += 1
    return sorted_list, inversion_number


def merge_sort(l):
    if len(l) == 1:
        return l, 0
    left, inv1 = merge_sort(l[:int(len(l) / 2)])
    right, inv2 = merge_sort(l[int(len(l) / 2):])
    sorted_list, inversion_num = Merge_list(left, right)
    return sorted_list, inversion_num + inv1 + inv2


# print(merge_sort([5, 4, 3, 2, 1]))


def get_number_of_inversions(a, b, left, right):
    sorted_l, inversion_num = merge_sort(a)
    return inversion_num

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))

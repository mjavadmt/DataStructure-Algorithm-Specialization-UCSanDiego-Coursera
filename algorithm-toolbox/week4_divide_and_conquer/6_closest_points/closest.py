# # Uses python3
# import sys
# import math
#
#
# #
# # def Merge_list_x(left_list, right_list):
# #     sorted_list = []
# #     so_far_right = 0
# #     so_far_left = 0
# #     while so_far_left != len(left_list) or so_far_right != len(right_list):
# #         if so_far_left != len(left_list) and so_far_right != len(right_list):
# #             if left_list[so_far_left][0] > right_list[so_far_right][0]:
# #                 sorted_list.append(right_list[so_far_right])
# #                 so_far_right += 1
# #             else:
# #                 sorted_list.append(left_list[so_far_left])
# #                 so_far_left += 1
# #         else:
# #             if so_far_left != len(left_list):
# #                 sorted_list.append(left_list[so_far_left])
# #                 so_far_left += 1
# #             if so_far_right != len(right_list):
# #                 # dont do anything
# #                 sorted_list.append(right_list[so_far_right])
# #                 so_far_right += 1
# #     return sorted_list
# #
# #
# # def Merge_list_y(left_list, right_list):
# #     sorted_list = []
# #     so_far_right = 0
# #     so_far_left = 0
# #     while so_far_left != len(left_list) or so_far_right != len(right_list):
# #         if so_far_left != len(left_list) and so_far_right != len(right_list):
# #             if left_list[so_far_left][1] > right_list[so_far_right][1]:
# #                 sorted_list.append(right_list[so_far_right])
# #                 so_far_right += 1
# #             else:
# #                 sorted_list.append(left_list[so_far_left])
# #                 so_far_left += 1
# #         else:
# #             if so_far_left != len(left_list):
# #                 sorted_list.append(left_list[so_far_left])
# #                 so_far_left += 1
# #             if so_far_right != len(right_list):
# #                 sorted_list.append(right_list[so_far_right])
# #                 so_far_right += 1
# #     return sorted_list
# #
# #
# # def merge_sort_x(l):
# #     if len(l) == 1:
# #         return l
# #     left = merge_sort_x(l[:int(len(l) / 2)])
# #     right = merge_sort_x(l[int(len(l) / 2):])
# #     sorted_list = Merge_list_x(left, right)
# #     return sorted_list
# #
# #
# # def merge_sort_y(l):
# #     if len(l) == 1:
# #         return l
# #     left = merge_sort_y(l[:int(len(l) / 2)])
# #     right = merge_sort_y(l[int(len(l) / 2):])
# #     sorted_list = Merge_list_y(left, right)
# #     return sorted_list
#
#
# # print(merge_sort_y([[7, 7], [1, 100], [4, 8], [7, 7]]))
#
#
# def find_distance(p1, p2):
#     return round(((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5, 5)
#
#
# def find_between(between, min_so_far):
#     for i in range(len(between)):
#         move = i + 7
#         if i + 7 > len(between):
#             move = len(between)
#         for j in range(i + 1, move):
#             check_distance = find_distance(between[i], between[j])
#             if check_distance < min_so_far:
#                 min_so_far = check_distance
#     return min_so_far
#
#
# def find_minimum_distance_points(l):
#     if len(l) == 3:
#         first_d = find_distance(l[0], l[1])
#         second_d = find_distance(l[0], l[2])
#         third_d = find_distance(l[1], l[2])
#         return min(first_d, second_d, third_d)
#     if len(l) == 2:
#         return find_distance(l[0], l[1])
#     first_half = l[:len(l) // 2]
#     second_half = l[len(l) // 2:]
#     x_middle = (first_half[-1][0] + second_half[0][0]) / 2
#     a = find_minimum_distance_points(first_half)
#     b = find_minimum_distance_points(second_half)
#     min_ab = min(a, b)
#     check_between = []
#     for i in range(1, len(first_half) + 1):
#         if x_middle - first_half[-i][0] > min_ab:
#             break
#         check_between.append(first_half[-i])
#     for i in range(len(second_half)):
#         if second_half[i][0] - x_middle > min_ab:
#             break
#         check_between.append(second_half[i])
#
#     check_between = sorted(check_between, key=lambda e: e[1])
#     min_ab = find_between(check_between, min_ab)
#     return min_ab
#
#
# # for_left = True
# # for_right = True
# # for i in range(1, len(l) + 1):
# #     if for_left:
# #         if i <= len(first_half) + 1 and x_middle - first_half[-i][0] <= min_ab:
# #             check_between.append(first_half[-i])
# #         else:
# #             for_left = False
# #         if i == len(first_half):
# #             for_left = False
# #     if for_right:
# #         if i < len(second_half) and second_half[i-1][0] - x_middle <= min_ab:
# #             check_between.append(second_half[i-1])
# #         else:
# #             for_right = False
# #         if i - 1 == len(second_half) - 1:
# #             for_right = False
# #     if not for_left and not for_right:
# #         break
#
# # list_to_find = [[4, 4], [-2, -2], [-1, 3], [2, 3], [-3, -4], [-4, 0], [1, 1], [-1, -1], [3, -1], [-4, 2], [-2, 4]]
# # list_to_find = sorted(list_to_find, key=lambda e: e[0])
# # var1 = list_to_find[1::2]
# # var2 = list_to_find[2::2]
#
#
# # print(find_minimum_distance_points(list_to_find))
#
#
# def minimum_distance(x, y):
#     points = []
#     for i in range(len(x)):
#         points.append([x[i], y[i]])
#     points = sorted(points, key=lambda e: e[0])
#     return find_minimum_distance_points(points)
#
#
# # print(minimum_distance(var1, var2))
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n = data[0]
#     x = data[1::2]
#     y = data[2::2]
#     print("{0:.9f}".format(minimum_distance(x, y)))


# Uses python3
import sys
import math
import random


# sorting

def partition3(a, l, r, index):
    # write your code here
    x = a[l][index]
    j = l
    for i in range(l + 1, r + 1):
        if a[i][index] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    k = inverse_partition3(a, l, j, index)
    # a[l], a[k] = a[k], a[l]

    return k, j


def inverse_partition3(a, l, r, index):
    x = a[l][index]
    j = l
    for i in range(l + 1, r + 1):
        if a[i][index] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r, index):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m, n = partition3(a, l, r, index)
    randomized_quick_sort(a, l, m - 1, index)
    randomized_quick_sort(a, n + 1, r, index)


def minimum_distance_y(my_list, d):
    randomized_quick_sort(my_list, 0, len(my_list) - 1, 1)
    for i in range(len(my_list) - 1):
        max_index = i + 7
        if len(my_list) < i + 7:
            max_index = len(my_list)

        for j in range(i + 1, max_index):
            distance = ((my_list[i][0] - my_list[j][0]) ** 2 + (my_list[i][1] - my_list[j][1]) ** 2) ** 0.5
            if distance < d:
                d = distance
    return d


# def minimum_distance_y(my_list,d):
#     for i in range(len(my_list)-1):
#         for j in range(i+1,len(my_list)):
#             distance=((my_list[i][0]-my_list[j][0])**2+(my_list[i][1]-my_list[j][1])**2)**0.5
#             if distance<d:
#                 d=distance
#     return d


def minimum_distance(my_list):
    # write your code here
    # return 10 ** 18
    if len(my_list) == 3:
        distanve1 = ((my_list[1][0] - my_list[0][0]) ** 2 + (my_list[1][1] - my_list[0][1]) ** 2) ** 0.5
        distanve2 = ((my_list[2][0] - my_list[0][0]) ** 2 + (my_list[2][1] - my_list[0][1]) ** 2) ** 0.5
        distance3 = ((my_list[1][0] - my_list[2][0]) ** 2 + (my_list[1][1] - my_list[2][1]) ** 2) ** 0.5
        min = distanve1
        for i in [distanve2, distance3]:
            if min > i:
                min = i
        return min
    if len(my_list) == 2:
        distanve1 = ((my_list[1][0] - my_list[0][0]) ** 2 + (my_list[1][1] - my_list[0][1]) ** 2) ** 0.5
        return distanve1
    ave = int(len(my_list) / 2)
    a1 = []
    a2 = []
    for item in range(ave):
        a1.append(my_list[item])

    for item2 in range(ave, len(my_list)):
        a2.append(my_list[item2])
    d1 = minimum_distance(a1)
    d2 = minimum_distance(a2)
    d = 0
    if d1 >= d2:
        d = d2
    else:
        d = d1
    min = my_list[ave][0] - d
    max = my_list[ave][0] + d
    new_list = []
    for j in my_list:
        if (j[0] > min and j[0] < max):
            new_list.append(j)
    my_list = new_list

    minimum_d = minimum_distance_y(my_list, d)
    return minimum_d


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    my_list = []
    for i in range(n):
        my_list.append([x[i], y[i]])
    randomized_quick_sort(my_list, 0, len(my_list) - 1, 0)
    print("{0:.9f}".format(minimum_distance(my_list)))



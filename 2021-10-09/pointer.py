# -*- coding:utf-8 -*- #
# @time 2021-10-09 22:24
# author:pengda

"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

"""


def sorted_squares(nums):
    new_nums = list(map(lambda x: x ** 2, nums))
    return sorted(new_nums)


print(sorted_squares([-4, -1, 0, 3, 10]))


"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
"""


def rotate(nums: list, k: int):
    while k > 0:
        nums_value = nums.pop()
        nums.insert(0, nums_value)
        k -= 1
    return nums


print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
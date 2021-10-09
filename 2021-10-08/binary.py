# -*- coding:utf-8 -*- #
# @time 2021/10/8 22:05
# @author:pengda

"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

"""
from typing import List

alist = [-1, 0, 3, 5, 9, 12, 15]
blist = [-1, 0, 3, 5, 9, 12]


def search(nums: List[int], target: int) -> int:
    left_index = 0
    right_index = len(nums) - 1

    while left_index < right_index:
        mid_index = int((right_index - left_index) / 2 + left_index)
        mid_nums = nums[mid_index]
        if mid_nums == target:
            return mid_index
        elif mid_nums < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index
    return -1


assert search(alist, 12) == 5
assert search(alist, 2) == -1


"""
第一个错误的版本

你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

"""


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    start_version = 1
    end_version = n

    while start_version < end_version:
        mid_version = (end_version - start_version) // 2 + start_version
        if isBadVersion(mid_version) is True:
            end_version = mid_version
        else:
            start_version = mid_version + 1
    return start_version


def isBadVersion(x):
    if x >= 4:
        return True
    else:
        return False


assert firstBadVersion(8) == 4


def searchInsert(nums: List[int], target: int) -> int:
    left_index = 0
    right_index = len(nums) - 1

    if nums[right_index] < target:
        return right_index + 1

    if nums[0] > target:
        return 0

    while left_index <= right_index:
        mid_index = int((right_index - left_index) / 2 + left_index)
        mid_nums = nums[mid_index]
        if mid_nums == target:
            return mid_index
        elif mid_nums < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return left_index


print(searchInsert(alist, 22))
print('pass')


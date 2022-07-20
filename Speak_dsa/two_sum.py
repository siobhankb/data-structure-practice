# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]



# Follow-up: 
# Can you come up with an algorithm that is less than O(n^2) time complexity?

import enum
import itertools


def twoSum(nums, target):
    for a, b in itertools.product(nums, nums):
        if a + b == target:
            return [nums.index(a), nums.index(b)]

nums1 = [2,11,15,7]
target1 = 9

# test1 = twoSum(nums1, target1)
# print(test1)

nums2 = [3,3]
target2 = 6

# test2 = twoSum(nums2, target2)
# print(test2)
# results in [0,0] bc .index() only finds FIRST index :(

#DIY solution:
# use "subsets" algo pattern
# still O(n^2) bc while loop...
def twoSumOn2(nums, target):
    length = len(nums)
    n = 0
    while n <= length - 1:
        match = target - nums[n]
        for i in range(n + 1, length):
            if nums[n] + nums[i] == target:
                return [n,i]
        n += 1

nums2 = [3,3]
target2 = 6

# test2 = twoSumOn2(nums2, target2)
# print(test2)

# test3 = twoSumOn2(nums1, target1)
# print(test3)

def twoSumOofN(nums, target):
    length = len(nums)
    checkMap = {}
    for i, n in enumerate(nums):
        match = target - n
        if match in checkMap:
            return [checkMap[match], i]
        checkMap[n] = i
    return

nums4 = [2,11,15,7]
target4 = 9

test4 = twoSumOofN(nums4, target4)
print(test4)

test5 = twoSumOofN(nums2, target2)
print(test5)
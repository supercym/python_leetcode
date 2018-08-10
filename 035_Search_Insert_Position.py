# Author: cym


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target <= nums[0]:
        return 0
    if target > nums[len(nums)-1]:
        return len(nums)
    ans = 0
    for i, v in enumerate(nums):
        if v >= target:
            ans = i
            break
    return ans


print(searchInsert([1,3,5,6], 5))
print('###################')
print(searchInsert([1,3,5,6], 2))
print('###################')
print(searchInsert([1,3,5,6], 7))
print('###################')
print(searchInsert([1,3,5,6], 0))
print('###################')
print(searchInsert([1,3,5,6], 6))


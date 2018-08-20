# Author: cym


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    for i in range(n):
        nums1 = insert_list(nums1, m, nums2[i])
        m += 1
    zero_num = len(nums1) - m
    for i in range(zero_num):
        nums1.pop()
    # 如果没有返回值的话
    # 最后用 nums1 = nums1[:8]，会显示前面那个nums1未被使用


# 二分查找、插入
def insert_list(nums, m, d):
    low = 0
    high = m-1

    while low <= high:
        if (high - low) < 2:
            if d < nums[low]:
                nums.insert(low, d)
            elif d > nums[high]:
                nums.insert(high+1, d)
            else:
                nums.insert(high, d)
            break
        mid = int((low + high)/2)
        tmp = nums[mid]
        if tmp == d:
            nums.insert(mid, d)
            break
        if tmp > d:
            high = mid - 1
        else:
            low = mid + 1
    return nums

if __name__ == "__main__":
    nums = [4,5,7,0,0,0]
    merge(nums, 3, [1,6,99], 3)
    print(nums)






# Author: cym

def maxArea(height: 'List[int]') -> 'int':
        i, j = 0, len(height)-1
        h = min(height[i], height[j])
        flag = True if height[i] < height[j] else False
        maxwater = h*(j-i)

        while True:
            if flag:
                while i < len(height) and height[i] <= h:
                    i += 1
            else:
                while j > 0 and height[j] <= h:
                    j -= 1
            if i >= j:
                break
            h = min(height[i], height[j])
            maxwater = max(h*(j-i), maxwater)
            flag = True if height[i] < height[j] else False

        return maxwater

nums = [1,8,6,2,5,4,8,3,7]
print(maxArea(nums))


class Solution:
    def nextGreaterElements(self, nums):
        size = len(nums)
        nums.extend(nums)
        result = [-1] * len(nums)
        stack = []
        for i in range(0,len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                result[index] = nums[i]
            stack.append(i)
        return result[:size]
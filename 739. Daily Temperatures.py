class Solution:
    def dailyTemperatures(self, nums):
        result = [0] * len(nums)
        stack = []
        for i in range(0,len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                result[index] = i - index 
            stack.append(i)
        return result
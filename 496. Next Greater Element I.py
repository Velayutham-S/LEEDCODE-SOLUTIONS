class Solution:
    def nextGreaterElement(self,nums1,nums):
        result = [-1] * len(nums)
        stack = []
        for i in range(0,len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                result[index] = nums[i]
            stack.append(i)
        final = []
        for i in nums1:
            index = nums.index(i)
            final.append(result[index])
        return final
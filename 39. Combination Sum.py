class Solution:
    def __init__(self):
        self.final = []
    def combinationSum(self, candidates, target):
        def findsum(x, nums, list1, remaining):
            if remaining == 0:
                self.final.append(list1.copy())
                return
            if x >= len(nums):
                return
            if remaining < 0:
                return
            list1.append(nums[x])
            findsum(x, nums, list1, remaining - nums[x])
            list1.pop()
            findsum(x + 1, nums, list1, remaining)
        findsum(0, candidates, [], target)
        return self.final
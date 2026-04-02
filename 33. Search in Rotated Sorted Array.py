class Solution:
    def search(self, nums, target) -> int:
        index1 = -1
        if target in nums:
            index1 = nums.index(target)
            return index1
        return -1
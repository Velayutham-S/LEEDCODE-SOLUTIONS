# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = []
        def levelOrderRec(root, level, res):
            if root is None:
                return
            if len(res) <= level:
                res.append([])
            res[level].append(root.val)
            levelOrderRec(root.left, level + 1, res)
            levelOrderRec(root.right, level + 1, res)
        levelOrderRec(root,0,res)
        max_sum = float('-inf')
        index1 = -1
        for i in range(0,len(res)):
            if sum(res[i]) > max_sum:
                max_sum = max(max_sum,sum(res[i]))
                index1 = i
        return index1 + 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int):
        def path(node,sum1,target):
            if not node:
                return
            sum1 += node.val
            if not node.left and not node.right:
                if sum1 == target:
                    return True
            else:
                if path(node.left,sum1,target):
                    return True
                if path(node.right,sum1,target):
                    return True
        value = path(root,0,targetSum)
        if value:
            return True
        return False


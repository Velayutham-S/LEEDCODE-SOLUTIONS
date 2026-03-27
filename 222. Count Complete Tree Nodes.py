# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):
        res = []
        if not root:
            return 0
        def path(node,count):
            if not node:
                return
            count += 1
            if not node.left and not node.right:
                res.append(count)
            else:
                path(node.left,count)
                path(node.right,count)
        path(root,0)
        return min(res)
        
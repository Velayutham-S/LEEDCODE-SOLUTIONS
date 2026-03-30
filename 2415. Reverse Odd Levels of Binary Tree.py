# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        def construct(left1,right1,level):
            if not left1 and not right1:
                return
            if level % 2 == 0:
                left1.val,right1.val = right1.val,left1.val
            construct(left1.left,right1.right,level+1)
            construct(left1.right,right1.left,level+1)
        construct(root.left,root.right,0)
        return root
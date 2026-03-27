# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        res = []
        def path(node,target,res,temp):
            if not node:
                return
            temp.append(node.val)
            if not node.left and not node.right:
                if sum(temp) == target:
                    res.append(temp[:])
                    print(res)
            else:
                path(node.left,target,res,temp)
                path(node.right,target,res,temp)
            temp.pop()
        value = path(root,targetSum,res,[])
        return res
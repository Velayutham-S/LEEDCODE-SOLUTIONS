# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        res = []
        def treepaths(node,path,res):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                res.append(path)
            else:
                treepaths(node.left,path+"->",res)
                treepaths(node.right,path+"->",res)
        treepaths(root,"",res)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def levelorder(node,level):
            if not node:
                return
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
            levelorder(node.left,level+1)
            levelorder(node.right,level+1)
        levelorder(root,0)
        final = []
        for i in range(0,len(res)):
            final.append(sum(res[i]))
        final.sort(reverse = True)
        if k <= len(final):
            return final[k - 1]
        return - 1
        
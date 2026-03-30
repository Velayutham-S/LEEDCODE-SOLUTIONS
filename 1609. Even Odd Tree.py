# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root):
        res = []
        def levelorder(node,level):
            if not node:
                return
            if len(res) <= level:
                res.append([])
            if level % 2 == 0 and node.val % 2 != 0 and node.val not in res[level]:
                res[level].append(node.val)
            elif level % 2 != 0 and node.val % 2 == 0 and node.val not in res[level]:
                res[level].append(node.val)
            else:
                return False
            final = levelorder(node.left,level+1)
            if final == False:
                return False
            final = levelorder(node.right,level+1)
            if final == False:
                return False
        final = levelorder(root,0)
        if final == False:
            return False
        for i in range(0,len(res)):
            if i % 2 == 0 and sorted(res[i]) == res[i]:
                continue
            elif i % 2 != 0  and sorted(res[i],reverse = True) == res[i]:
                continue
            else:
                return False
        return True
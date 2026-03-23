# Solution 1:
class Solution:
    def minDiffInBST(self, root):
        if not root:
            return
        res = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        ans = []
        inorder(root)
        print(res)
        if len(res) >= 2:
            for i in range(0,len(res)):
                for j in range(i+1,len(res)):
                    ans.append(res[j] - res[i])
            return min(ans)
        return None
    
# Solution 2:

class Solution:
    def minDiffInBST(self, root):
        if not root:
            return
        res = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        ans = []
        inorder(root)
        print(res)
        if len(res) >= 2:
            for i in range(0,len(res)):
                for j in range(i+1,len(res)):
                    ans.append(res[j] - res[i])
            return min(ans)
        return None


        
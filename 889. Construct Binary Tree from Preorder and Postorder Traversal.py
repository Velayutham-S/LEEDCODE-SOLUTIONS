class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        if not preorder or not postorder:
            return None

        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        root_left = postorder.index(preorder[1]) + 1

        root.left = self.constructFromPrePost(
            preorder[1:1 + root_left],
            postorder[:root_left]
        )

        root.right = self.constructFromPrePost(
            preorder[1 + root_left:],
            postorder[root_left:-1]
        )

        return root
class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        left_leaves = []
        right_leaves = []

        def helper(node, leaves):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
            helper(node.left, leaves)
            helper(node.right, leaves)

        helper(root1, left_leaves)
        helper(root2, right_leaves)

        return left_leaves == right_leaves
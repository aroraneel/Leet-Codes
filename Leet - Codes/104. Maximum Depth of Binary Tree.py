from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(3,
                    TreeNode(9),
                    TreeNode(20, TreeNode(15), TreeNode(7)))

    result = sol.maxDepth(root)

    print("Maximum Depth of Tree:", result)

    # Summary:
    # This program calculates the maximum depth of a binary tree.
    # It recursively finds the depth of left and right subtrees.
    # The depth is the larger of the two subtree depths plus one for the root.
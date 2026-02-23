from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def chk(root):
            if root.left is None and root.right is None:
                return 1
            elif root.left is not None and root.right is None:
                return chk(root.left) + 1
            elif root.left is None and root.right is not None:
                return chk(root.right) + 1
            else:
                return min(chk(root.left), chk(root.right)) + 1

        return chk(root)


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1,
                    TreeNode(2,
                             TreeNode(4),
                             None),
                    TreeNode(3))

    result = sol.minDepth(root)

    print("Minimum Depth of Tree:", result)

    # Summary:
    # This program calculates the minimum depth of a binary tree.
    # Minimum depth is the shortest path from root to a leaf node.
    # It carefully handles cases where one child is missing.
    # The result is the minimum depth among valid child paths plus one.
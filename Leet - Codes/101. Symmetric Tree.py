from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def chk(a, b):
            if a is None and b is None:
                return True

            if a is None or b is None:
                return False

            return (a.val == b.val and
                    chk(a.left, b.right) and
                    chk(a.right, b.left))

        return chk(root, root)


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1,
                    TreeNode(2, TreeNode(3), TreeNode(4)),
                    TreeNode(2, TreeNode(4), TreeNode(3)))

    result = sol.isSymmetric(root)

    print("Is the tree symmetric?", result)

    # Summary:
    # This program checks whether a binary tree is symmetric.
    # It compares the left and right subtrees recursively.
    # For symmetry, the left subtree of one side must match
    # the right subtree of the other side and vice versa.
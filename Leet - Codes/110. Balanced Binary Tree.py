from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def chk(root):
            if root is None:
                return 0

            l = chk(root.left)
            r = chk(root.right)

            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            else:
                return 1 + max(l, r)

        return chk(root) != -1


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(3,
                    TreeNode(9),
                    TreeNode(20, TreeNode(15), TreeNode(7)))

    result = sol.isBalanced(root)

    print("Is the tree balanced?", result)

    # Summary:
    # This program checks whether a binary tree is height-balanced.
    # A tree is balanced if the height difference between left and right subtrees
    # is not more than 1 at every node.
    # It returns -1 if an imbalance is found, otherwise returns the height.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def chk(root, target):
            if root is None:
                return False

            if root.val == target and root.left is None and root.right is None:
                return True

            return (chk(root.left, target - root.val) or
                    chk(root.right, target - root.val))

        return chk(root, targetSum)


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(5,
                    TreeNode(4,
                             TreeNode(11, TreeNode(7), TreeNode(2))),
                    TreeNode(8,
                             TreeNode(13),
                             TreeNode(4, None, TreeNode(1))))

    targetSum = 22
    result = sol.hasPathSum(root, targetSum)

    print("Target Sum:", targetSum)
    print("Has Path Sum?", result)

    # Summary:
    # This program checks whether there exists a root-to-leaf path
    # whose values sum up to the given target.
    # It recursively subtracts the current node value from the target
    # and checks both left and right subtrees.
    # If a leaf node matches the remaining sum, it returns True.
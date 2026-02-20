from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


if __name__ == "__main__":
    sol = Solution()

    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))

    result = sol.isSameTree(p, q)

    print("Are the two trees the same?", result)

    # Summary:
    # This program checks whether two binary trees are identical.
    # Two trees are the same if they have the same structure
    # and the same node values at every position.
    # It uses recursion to compare left and right subtrees.
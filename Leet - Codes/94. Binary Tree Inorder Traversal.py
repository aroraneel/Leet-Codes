from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    result = sol.inorderTraversal(root)

    print("Inorder Traversal:", result)

    # Summary:
    # This program performs an inorder traversal of a binary tree.
    # In inorder traversal, nodes are visited in the order:
    # left subtree -> root -> right subtree.
    # It uses recursion to collect values in the result list.

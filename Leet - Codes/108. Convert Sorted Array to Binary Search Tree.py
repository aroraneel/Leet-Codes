from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


if __name__ == "__main__":
    sol = Solution()

    nums = [-10, -3, 0, 5, 9]
    root = sol.sortedArrayToBST(nums)

    print("Inorder Traversal of BST:")
    inorder(root)
    print()

    # Summary:
    # This program converts a sorted array into a height-balanced BST.
    # It selects the middle element as the root.
    # The left half forms the left subtree and the right half forms the right subtree.
    # This ensures the tree remains balanced.
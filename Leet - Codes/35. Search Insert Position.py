class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 3, 5, 6]
    target = 5

    result = sol.searchInsert(nums, target)

    print("Array:", nums)
    print("Target:", target)
    print("Insert Position:", result)

    # Summary:
    # This program finds the index where the target should be inserted in a sorted array.
    # It uses binary search to efficiently locate the target or the correct insertion point.
    # If the target exists, its index is returned; otherwise, the position to insert is returned.

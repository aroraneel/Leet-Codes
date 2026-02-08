from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 1, 2, 2, 3, 4, 4]
    k = sol.removeDuplicates(nums)

    print("Array after removing duplicates:", nums[:k])
    print("Number of unique elements:", k)

    # Summary:
    # This program removes duplicates from a sorted array in-place.
    # It uses two pointers: one to track the position of unique elements
    # and the other to scan through the array.
    # The function returns the count of unique elements.

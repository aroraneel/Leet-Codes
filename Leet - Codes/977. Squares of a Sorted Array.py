from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = [i * i for i in nums]
        lst.sort()
        return lst


if __name__ == "__main__":
    sol = Solution()

    nums = [-4, -1, 0, 3, 10]
    result = sol.sortedSquares(nums)

    print("Original Array:", nums)
    print("Sorted Squares:", result)

    # Summary:
    # This program returns the squares of each number in a sorted array.
    # It first squares all elements using a list comprehension.
    # Then it sorts the squared values.
    # The final sorted list is returned.
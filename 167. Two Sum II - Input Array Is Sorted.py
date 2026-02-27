from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            totalsum = numbers[left] + numbers[right]

            if totalsum > target:
                right -= 1
            elif totalsum < target:
                left += 1
            else:
                return [left + 1, right + 1]


if __name__ == "__main__":
    sol = Solution()

    numbers = [2, 7, 11, 15]
    target = 9
    result = sol.twoSum(numbers, target)

    print("Numbers:", numbers)
    print("Target:", target)
    print("Indexes (1-based):", result)

    # Summary:
    # This program finds two numbers in a sorted array that add up to the target.
    # It uses the two-pointer technique starting from both ends.
    # If the sum is too large, move the right pointer left.
    # If the sum is too small, move the left pointer right.
    # It returns 1-based indexes of the two numbers.
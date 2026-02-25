from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    sol = Solution()

    nums = [4, 1, 2, 1, 2]
    result = sol.singleNumber(nums)

    print("Array:", nums)
    print("Single Number:", result)

    # Summary:
    # This program finds the element that appears only once in the array.
    # It uses XOR operation where:
    # a ^ a = 0 and a ^ 0 = a.
    # All duplicate numbers cancel out,
    # leaving only the number that appears once.
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            result += [i + [num] for i in result]

        return result


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 3]
    result = sol.subsets(nums)

    print("Numbers:", nums)
    print("Subsets:", result)

    # Summary:
    # This program generates all possible subsets (power set) of a list of numbers.
    # It starts with an empty subset and for each number,
    # it creates new subsets by adding the number to existing ones.
    # The final result contains all subset combinations.
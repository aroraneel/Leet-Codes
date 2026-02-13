from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in nums:
                if i not in path:
                    path.append(i)
                    backtrack(path)
                    path.pop()

        backtrack([])
        return result


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 3]
    result = sol.permute(nums)

    print("Numbers:", nums)
    print("Permutations:", result)

    # Summary:
    # This program generates all possible permutations of a list of numbers.
    # It uses backtracking to build each permutation step by step.
    # A number is added to the current path only if it is not already used.
    # When the path length equals the nums length, a complete permutation is stored.

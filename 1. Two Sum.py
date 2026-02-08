class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    sol = Solution()

    nums = [2, 4, 6, 1]
    target = 3

    result = sol.twoSum(nums, target)

    print("Array:", nums)
    print("Target:", target)
    print("Indexes:", result)

    # Summary:
    # This program finds two numbers in the list that add up to the target value.
    # It checks every possible pair using two nested loops.
    # When a matching pair is found, it returns their indexes.

